import platform
from typing import List, Tuple, Any, Optional, Literal
import sys
import shutil
import argparse
import subprocess
import os
from pathlib import Path
import re
from collections import Counter
import json
from multiprocessing import Pool, Process, Value
from concurrent.futures import ProcessPoolExecutor
import logging
from multiprocessing import Manager
from utils_llm import get_commercial_model, prompt_commercial_model
from utils import patch_jpype
from manager import get_manager

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def remove_java_comments(java_code):
    # Remove multi-line comments (/* ... */)
    java_code_no_multiline = re.sub(r'/\*[\s\S]*?\*/', '', java_code)

    # Remove single-line comments (// ...)
    java_code_no_comments = re.sub(r'//.*', '', java_code_no_multiline)

    return java_code_no_comments

# def get_llm_prompt_by_src_code(src_code):
#     prompt = f"""Given a piece of Java source code. Please analyze it to determine if JMH benchmark tests are needed. If necessary, generate the corresponding JMH benchmark code in throughput benchmark mode for performance measurement, embedding relevant knowledge and best practices for performance testing in the generated code.

# Source Code:
# {src_code}

# Output instructions:
# + If it's not necessary to generate JMH code, output SKIP with reasons
# + If it's necessary to generate JMH code:
#   - Do not add any explanation or commentary before or after the test code.
#   - Wrap the entire code inside triple backticks like this:
#   ```
#   // your code here
#   ```
# """
#     return prompt

def get_llm_repair_prompt(code, err_msg):
    prompt = f"""Fix the bug in JMH code according to the runtime exception

JMH Code:
{code}

Runtime Message:
{err_msg}

Output instructions:
  - Do not add any explanation or commentary before or after the test code.
  - Wrap the entire code inside triple backticks like this:
  ```
  // your code here
  ```
"""
    return prompt

def generate_performance_tests(model: str, prompt: str) -> str:
    client = get_commercial_model(model)
    resp = prompt_commercial_model(client, model, prompt, image_id="")
    return resp

def generate_performance_tests_wrapper(args: Tuple[Any]):
    jmh_file, source_file, model, save_path, err_msg = args
    if save_path.exists() and save_path.stat().st_size > 0:
        logging.info(f"{str(save_path)} is generated from model {model}, skip")
        return

    save_path.parent.mkdir(exist_ok=True, parents=True)
    with open(jmh_file, 'r') as fd:
        jmh_code = fd.read()

    pure_jmh_code = remove_java_comments(jmh_code)
    code_with_prompt = get_llm_repair_prompt(pure_jmh_code, err_msg)
    _args = (model, code_with_prompt)
    logging.info(f"Will save the response into save_path: {save_path}")
    raw_resp = generate_performance_tests(*_args)
    with open(save_path, 'w') as fd:
        fd.write(raw_resp)


def main(args):
    root_branch = {
        'rxjava': 'jmh',
        'eclipse-collections': 'jmh-tests',
        'zipkin': 'benchmarks'
    }
    project = args.project
    mgr = get_manager(project, root_branch[project])
    src_dirs = mgr.src_dirs
    model = args.model
    strategy = args.strategy
    if strategy is None:
        save_dir = Path(f'results/projects/{project}/generated/{model}')
    else:
        save_dir = Path(f'results/projects/{project}/generated/{model}-{strategy}')
    to_branch = args.to_branch

    repair_cnt = args.repair_cnt

    with open(save_dir / f'repair-list-{repair_cnt}.json', 'r') as fd:
        code_need_repair = json.load(fd)

    pkg_file_to_src_dir = {str(x.relative_to(src_dir)): src_dir for src_dir in src_dirs for x in src_dir.rglob('*.java')}
    args_list = []
    for code_path, err_msg in code_need_repair.items():
        code_path = Path(code_path)
        pkg_file = code_path.relative_to(save_dir)
        src_dir = pkg_file_to_src_dir.get(str(pkg_file))
        if src_dir is None:
            continue
        src_path = src_dir / pkg_file
        if not src_path.exists():
            logging.error("> BUG: wrong configuration")

        save_path = save_dir / f'{str(src_path.relative_to(src_dir))}.repair-{repair_cnt}.txt'
        _args = (code_path, src_path, model, save_path, err_msg)
        args_list.append(_args)

    if args.parallel:
        with Pool(8) as pool:
            pool.map(generate_performance_tests_wrapper, args_list)
        pool.join()
    else:
        for _args in args_list:
            generate_performance_tests_wrapper(_args)


if __name__ ==  "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=True, help='rxjava, eclipse-collections, zipkin')
    parser.add_argument("--to_branch", type=str, default='llm2jmh')
    parser.add_argument("--model", type=str, default='deepseek-chat')
    parser.add_argument("--strategy", type=str, default=None, help='with-junit')
    parser.add_argument('--parallel', action='store_true')
    parser.add_argument('--repair_cnt', type=int, default=0)
    args = parser.parse_args()

    main(args)
