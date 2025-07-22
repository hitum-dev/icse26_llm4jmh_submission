import platform
from typing import List, Optional
import sys
import argparse
import subprocess
import os
from pathlib import Path
import shutil
from collections import defaultdict
import zipfile
from collections import Counter
import re
import json
import pandas as pd
from multiprocessing import Pool, Process, Manager as ProcessManager
from multiprocessing.managers import SyncManager
from concurrent.futures import ProcessPoolExecutor
import logging

from utils import *
from manager import get_manager

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def run_jmh_method_wrapper(args):
    cmd, method, benchmark_dir, cpu_queue = args
    benchmark_res = benchmark_dir / f'{method}.json'
    if benchmark_res.exists() and benchmark_res.stat().st_size > 0:
        logging.info(f"Skip existed result of benchmark {method}")
        return

    cpus = cpu_queue.get()
    if platform.system() == 'Linux':
        cmd = taskset_wrapper(cmd, cpus)
    # setup_cgroup(f'{project}_{branch}_{method}', cpus)
    run_jmh_method(cmd)
    cpu_queue.put(cpus)


def run_jmh_method(cmd: str):
    logging.info(f"> Run command: {cmd}")
    timeout = 86400
    try:
        proc = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)
        # NOTE: attach it to cgroup if needed
        # Attach process to cgroup
        # with open(cgroup_path / "cgroup.procs", "w") as f:
        #     f.write(str(proc.pid))

        proc.wait(timeout=timeout)

        if proc.returncode != 0:
            logging.error(f"Command '{cmd}' failed with exit code {proc.returncode}.")
        else:
            logging.info(f"Command '{cmd}' finished successfully.")
    except subprocess.TimeoutExpired:
        logging.error(f"Command '{cmd}' timed out after {timeout} seconds.")
        proc.kill()
    except Exception as ex:
        logging.error(f'Command: {cmd}, unknown error: {str(ex)}')

def extract_methods_to_run(methods: List[str], branch: str, common_methods_path: Optional[Path]) -> List[str]:
    if common_methods_path is None:
        return methods

    splits = branch.split('_')
    if len(splits) == 4:
        base, bug, method, line = splits
        method = method.replace('-', '$')
        line = int(line)
    elif len(splits) == 1:
        # NOTE: I prefer running all common methods
        # base = splits[0]
        # method = "*"
        # line = -1
        return methods
    else:
        raise Exception(f"Unknown branch {branch}")

    df = pd.read_csv(str(common_methods_path))
    all_benchmarks = []
    for _, row in df.iterrows():
        method_line = eval(row['method'])
        if method == '*':
            benchmarks = row[base].split('|')
            all_benchmarks.extend(benchmarks)
        elif method_line[0] == method and method_line[1] == line:
            benchmarks = row[base].split('|')
            all_benchmarks.extend(benchmarks)
            break

    return all_benchmarks


def main(args):
    project = args.project
    branches = args.branch
    branch_to_mgr = {branch: get_manager(args.project, branch) for branch in branches}
    # mgr = get_manager(args.project, branch)

    cpu_queue = get_cpu_queue()
    # branch_to_args_list = {}
    args_list = []
    for branch, mgr in branch_to_mgr.items():
        benchmark_dir = mgr.save_benchmark_dir
        mgr.compile_if_needed(branch)
        jar_path = Path(f'./tmp/{mgr.cwd}/{branch}') / mgr.jar_path.name

        methods = mgr.list_benchmark_methods(jar_path)
        logging.info(f"Listing benchmark methods {len(methods)}")

        with open(benchmark_dir / '00-benchmark-methods.json', 'w') as f:
            json.dump(methods, f, indent=2)

        if args.benchmark is not None:
            methods = [x for x in methods if x in args.benchmark]
        else:
            methods = extract_methods_to_run(methods, branch, Path(args.common_methods_path) if args.common_methods_path else None)

        jvm_opts = "-Djmh.ignoreLock=true -Xms1g -Xmx8g"
        for method in methods:
            benchmark_res = benchmark_dir / f'{method}.json'
            cmd = f'java {jvm_opts} -jar {jar_path.resolve()} -f 1 -wi 5 -w 500ms -i 30 -r 1000ms -rf json -tu s -bm thrpt -gc true -rff {str(benchmark_res)} {method}'
            _args = (cmd, method, benchmark_dir, cpu_queue)
            args_list.append(_args)

        # branch_to_args_list[branch] = args_list

    # ##############################################
    if args.parallel:
        with ProcessPoolExecutor(max_workers=cpu_queue.qsize()) as executor:
            futures = []
            for _args in args_list:
                futures.append(executor.submit(run_jmh_method_wrapper, _args))

            for f in futures:
                f.result()  # Wait for all to complete
    else:
        for _args in args_list:
            run_jmh_method_wrapper(_args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=True, help='rxjava, eclipse-collections')
    parser.add_argument("--branch", action="append")
    parser.add_argument("--parallel", action="store_true")
    parser.add_argument("--benchmark", action='append', help='run specific benchmark method')
    parser.add_argument('--common_methods_path', type=str)
    args = parser.parse_args()

    main(args)
