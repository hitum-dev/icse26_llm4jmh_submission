import platform
from typing import List, Optional, Tuple, Any
import sys
import shutil
import subprocess
import os
from pathlib import Path
import zipfile
import re
import json
from xml.etree import ElementTree as ET
from termcolor import colored
from multiprocessing import Pool
from collections import defaultdict
import logging

from manager import get_manager

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def parse_jacoco_xml(file_path: Path):
    try:
        tree = ET.parse(file_path)
    except Exception as ex:
        # NOTE: fail to parse corrupted xml file
        file_path.unlink()
        return
    root = tree.getroot()
    packages = root.findall('package')
    coverage_data = defaultdict(list)
    detailed_coverage_data = defaultdict(list)
    for package in packages:
        classes = package.findall('class')
        for cls in classes:
            class_name = cls.get('name').replace('/', '.')
            methods = cls.findall('method')
            for method in methods:
                method_name = method.get('name')
                if '<' in method_name and '>' in method_name:
                    # Skip methods if generics
                    continue
                for counter in method.findall('counter'):
                    if int(counter.get('covered')) > 0:
                        try:
                            line_num = int(method.get('line'))
                            coverage_data[f"{class_name}.{method_name}"] = line_num
                            detailed_coverage_data[f"{class_name}.{method_name}"].append(dict(counter.items()))
                        except ValueError:
                            print(f'method_name: {method_name}')
                            import ipdb; ipdb.set_trace()

    return coverage_data, detailed_coverage_data


def main(args):
    jacoco_agent_jar = Path("deps/org.jacoco.agent-0.8.10-runtime.jar").resolve()

    branch = args.branch
    mgr = get_manager(args.project, args.branch)
    cwd = mgr.cwd
    save_dir = mgr.save_coverage_dir
    src_dirs = mgr.src_dirs
    class_dirs = mgr.class_dirs
    jar_path = mgr.jar_path

    logging.info(f"Checkout to branch {branch}")
    mgr.compile_if_needed(branch)
    methods = mgr.list_benchmark_methods(jar_path)
    logging.info(f"Listing benchmark {len(methods)} methods ...")
    args_list = []

    destfile_dir = save_dir / 'destfile'
    destfile_dir.mkdir(parents=True, exist_ok=True)
    benchmark_dir = save_dir / 'benchmark'
    benchmark_dir.mkdir(parents=True, exist_ok=True)
    log_dir = Path(f'logs/{cwd}/{branch}')
    log_dir.mkdir(parents=True, exist_ok=True)

    jmh_opts = "-i 1 -wi 0 -f 0 -r 100ms -rf json"
    for method in methods:
        destfile = destfile_dir / f'{method}.exec'
        # destfile = destfile_dir / f'00_all.exec'
        jacoco_agent_arg = f'-javaagent:{jacoco_agent_jar}=destfile={destfile},includes="{mgr.package}.*"'
        _args = (f'java -Djmh.ignoreLock=true {jacoco_agent_arg} -jar {jar_path} -jvmArgsAppend {jacoco_agent_arg} {jmh_opts}', method, benchmark_dir, log_dir)
        args_list.append(_args)

    args_list = args_list[:1]
    if args.parallel:
        with Pool(64) as pool:
            pool.map(run_jmh_method_wrapper, args_list)
        pool.join()
    else:
        for _args in args_list:
            run_jmh_method_wrapper(_args)

    class_dirs = mgr.unzip_jar_for_class_dirs()
    # class_dirs = mgr.class_dirs
    args_list = []

    for destfile in destfile_dir.glob('*.exec'):
        _args = (src_dirs, class_dirs, destfile)
        args_list.append(_args)

    if args.parallel:
        with Pool(64) as pool:
            pool.map(gen_xml_report_wrapper, args_list)
        pool.join()
    else:
        for _args in args_list:
            gen_xml_report_wrapper(_args)

    # gen_html_report_wrapper(args_list[0])


def run_jmh_method_wrapper(args: List[Tuple[Any]]):
    cmd, method, benchmark_dir, log_dir = args
    benchmark_res = benchmark_dir / f'{method}.json'
    logfile = log_dir / f'{method}.log'
    if benchmark_res.exists() and benchmark_res.stat().st_size > 0:
        logging.info(f"Skip existed result of benchmark {method}")
        return

    cmd = f'{cmd} -rff {str(benchmark_res)} {method}'
    run_jmh_method(cmd, logfile)


def run_jmh_method(cmd: str, logfile: Optional[Path] = None):
    logging.info(f"Running jmh method {cmd}")
    try:
        if logfile is not None:
            with open(logfile, 'w') as f:
                subprocess.run(
                    cmd,
                    check=True,
                    shell=True,
                    timeout=10,
                    stderr=subprocess.STDOUT,
                    stdout=f
                )
        else:
            subprocess.run(
                cmd,
                check=True,
                shell=True,
                timeout=10,
                stderr=subprocess.STDOUT
            )
    except subprocess.TimeoutExpired:
        logging.warning("The subprocess timed out and was terminated.")
    except Exception as ex:
        logging.error(f'Command: {cmd}, unknown error: {str(ex)}')


def gen_xml_report_wrapper(args: List[Tuple[Any]]):
    src_dirs, class_dirs, destfile = args
    json_path = destfile.parent.parent / destfile.with_suffix('.json').name
    detailed_json_path = destfile.parent.parent / destfile.with_suffix('.detailed.json').name
    xml_path = destfile.parent.parent / destfile.with_suffix('.xml').name

    if json_path.exists() and json_path.stat().st_size > 0 and detailed_json_path.exists() and detailed_json_path.stat().st_size > 0:
        return

    gen_xml_report(src_dirs, class_dirs, destfile)

    # NOTE: Analysis hit source code line by given benchmark method
    coverage_data, detailed_coverage_data = parse_jacoco_xml(xml_path)
    if len(coverage_data) == 0:
        logging.error(f"Fail to process file {str(xml_path)}, no hit line in source code")
        return

    logging.info(colored(f"process file {xml_path}", "green"))
    with open(json_path, 'w') as fd:
        json.dump(coverage_data, fd, indent=2)
        # NOTE: release the disk space otherwise it will run out of storage
    with open(detailed_json_path, 'w') as fd:
        json.dump(detailed_coverage_data, fd, indent=2)
    # xml_path.unlink()


def gen_xml_report(src_dirs: List[Path], class_dirs: List[Path], destfile: Path) -> Path:
    jacoco_cli_jar = Path("deps/org.jacoco.cli-0.8.13.jar").resolve()
    xml_path = destfile.parent.parent / destfile.with_suffix('.xml').name
    if xml_path.exists() and xml_path.stat().st_size > 0:
        return

    sourcefiles_args = ' '.join(f'--sourcefiles {d.resolve()}' for d in src_dirs)
    classfiles_args = ' '.join(f'--classfiles {d.resolve()}' for d in class_dirs)
    cmd = f'java -jar {jacoco_cli_jar} report {destfile.resolve()} {sourcefiles_args} {classfiles_args} --xml {xml_path.resolve()} --name {destfile.name}'

    logging.info(f"Gen report: {cmd}")
    try:
        subprocess.run(
            cmd,
            shell=True,
            check=True,
        )
    except subprocess.TimeoutExpired:
        logging.warning(colored("The subprocess timed out and was terminated.", "red"))
    except Exception as ex:
        logging.error(colored(f'Command: {cmd}, unknown error: {str(ex)}', "red"))

    return xml_path


def gen_html_report_wrapper(args: List[Tuple[Any]]):
    src_dirs, class_dirs, destfile = args
    gen_html_report(src_dirs, class_dirs, destfile)

def gen_html_report(src_dirs: List[Path], class_dirs: List[Path], destfile: Path):
    jacoco_cli_jar = Path("deps/org.jacoco.cli-0.8.13.jar").resolve()
    html_path = destfile.parent.parent / 'html'
    html_path.mkdir(parents=True, exist_ok=True)

    sourcefiles_args = ' '.join(f'--sourcefiles {d.resolve()}' for d in src_dirs)
    classfiles_args = ' '.join(f'--classfiles {d.resolve()}' for d in class_dirs)
    cmd = f'java -jar {jacoco_cli_jar} report {destfile.resolve()} {sourcefiles_args} {classfiles_args} --html {html_path.resolve()} --name {destfile.name}'
    logging.info(f"Gen report: {cmd}")
    try:
        subprocess.run(
            cmd,
            shell=True,
            check=True,
        )
    except subprocess.TimeoutExpired:
        logging.warning("The subprocess timed out and was terminated.")
    except Exception as ex:
        logging.error(f'unknown error: {str(ex)}')


# def gen_html_report(src_dir: Path, class_dir: Path, destfile: Path):
#     jacoco_jar = 'org.jacoco.cli-0.8.13.jar'
#     report_path = destfile.parent
#     cmd = f'java -jar {jacoco_jar} report {str(destfile)} --sourcefiles {str(src_dir)} --classfiles {str(class_dir)} --html {str(report_path)} --name {destfile.name}'
#     logging.info(f"Gen report: {cmd}")
#     cmd = cmd.split(' ')
#     try:
#         subprocess.run(
#             cmd,
#             check=True,
#             # timeout=300
#         )
#     except subprocess.TimeoutExpired:
#         logging.warning("The subprocess timed out and was terminated.")
#     except Exception as ex:
#         logging.error(f'unknown error: {str(ex)}')


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=True, help='rxjava, eclipse-collections')
    parser.add_argument("--branch", type=str, default='jmh')
    parser.add_argument("--parallel", action="store_true")
    args = parser.parse_args()

    main(args)
