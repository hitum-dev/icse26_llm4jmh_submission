import os
import subprocess
from typing import List, Optional
from pathlib import Path
from collections import defaultdict
from multiprocessing import Manager
from multiprocessing.managers import SyncManager
from itertools import chain


def map_logical_to_physical_cores():
    prefix = Path('/sys/devices/system/cpu')
    cpu_dirs = sorted([x for x in prefix.glob("cpu*") if x.is_dir()])
    core_map = defaultdict(list)

    for cpu_dir in cpu_dirs:
        try:
            cpu_num = int(cpu_dir.name[3:])
            with open(cpu_dir / 'topology/thread_siblings_list', 'r') as f:
                thread_siblings = sorted(list(map(int, f.read().strip().split(','))))
                if len(thread_siblings) != 2:
                    raise Exception("Incorrect number of hyperthreadings in cpu")

            with open(cpu_dir / 'topology/core_id', 'r') as f:
                core_id = int(f.read().strip())
            if thread_siblings not in core_map[core_id]:
                core_map[core_id].append(thread_siblings)
        except FileNotFoundError:
            pass
        except ValueError:
            pass
    return core_map


def setup_cgroup(group_name: str, cpus: List[int]):
    # TODO: not full test
    cgroup_root = "/sys/fs/cgroup"
    cpus_per_job = 4
    mem_per_job = 16 * 1024 ** 3  # 16 GB

    path = Path(cgroup_root) / group_name
    path.mkdir(parents=True, exist_ok=True)

    with open(path / "cgroup.subtree_control", "w") as f:
        f.write("+cpu +memory +cpuset\n")
    # Set allowed cpus for this group
    cpu_range = ','.join(map(str, cpus))
    with open(path / "cpuset.cpus", "w") as f:
        f.write(cpu_range)

    # Must assign memory nodes too (even just one node)
    with open(path / "cpuset.mems", "w") as f:
        f.write("0,1")

    # Set CPU max as soft limit (optional)
    with open(path / "cpu.max", "w") as f:
        f.write(f"{100000*cpus_per_job} 100000")

    # Set memory hard limit
    with open(path / "memory.max", "w") as f:
        f.write(str(mem_per_job))

    return path


def get_cpu_queue() -> 'SyncManager.Queue[List[int]]':
    # fokus maximum memory resource is 400GB
    max_mem = 400
    # fokus maximum cpu resource is 384
    max_cpus = 72
    cpus_per_task = 4
    mem_per_task = 8

    max_tasks = min(max_mem // mem_per_task, max_cpus // cpus_per_task)
    max_tasks = max(max_tasks, 50)

    manager = Manager()
    cpu_queue = manager.Queue()
    cpu_pairs = []

    try:
        core_map = map_logical_to_physical_cores()
        for v in core_map.values():
            flat = list(chain.from_iterable(v))
            if len(flat) < 4:
                raise Exception(f"Incorrect core threads {len(flat)}")
            flat = flat[:cpus_per_task]
            cpu_pairs.append(flat)
        if len(cpu_pairs) == 0:
            raise Exception(f"Cannot get cpu topology information")

    except Exception as ex:
        print(ex)
        import os
        num_cores = os.cpu_count()
        cpu_pairs = [[i + j for j in range(cpus_per_task)] for i in range(0, num_cores, cpus_per_task)]

    for cpu_pair in cpu_pairs:
        if cpu_queue.qsize() > max_tasks:
            break

        cpu_queue.put(cpu_pair)

    return cpu_queue


def taskset_wrapper(cmd: str, cpus: List[int]) -> str:
    cpu_range = ','.join(map(str, cpus))
    return f'taskset -c {cpu_range} {cmd}'


def compile_mutator():
    cmd = "mvn package"
    result = subprocess.run(
        cmd,
        check=True,
        shell=True,
        capture_output=True,  # captures stdout and stderr
        text=True,
    )
    return result


def patch_jpype(func):
    def wrapper(*args, **kwargs):
        import jpype
        import jpype.imports
        # from jpype.types import *
        # NOTE: `compile_mutator` is only used for `bug injector.py`, can comment it out if running other scripts
        # compile_mutator()
        project_root = Path(os.getcwd())
        classpath = []
        classpath.append(str(project_root / 'target/automator-guard-1.0-SNAPSHOT.jar'))
        javaparser_jar = str(Path("deps/javaparser-core-3.26.4.jar").resolve())
        classpath.append(javaparser_jar)
        if not jpype.isJVMStarted():
            jpype.startJVM(classpath=classpath)

        result = func(*args, **kwargs)

        jpype.shutdownJVM()
        return result
    return wrapper


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=False)
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    cpu_queue = get_cpu_queue()
    print("cpu queue size: ", cpu_queue.qsize())
    cpus = cpu_queue.get()
    print("cpus: ", cpus)
