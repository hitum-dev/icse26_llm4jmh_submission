import re
import math
import time
import pandas as pd
import numpy as np
from collections import defaultdict
from pathlib import Path
from manager import get_manager
import json
from typing import List, Dict, TypedDict, Optional
import logging

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main(args):
    branch = args.branch
    project = args.project
    mgr = get_manager(project, args.branch)
    cwd = mgr.cwd
    log_dir = Path(f'logs/projects/{project}/{branch}')
    logs = [x for x in log_dir.rglob("*.log")]

    maybe_error_benchmarks = []
    # pattern = re.compile(
    #     r"(java\.[\w.]+Exception|Error)[^\n]*\n(?:\s+at .+\n)+",
    #     re.MULTILINE
    # )
    pattern = re.compile(
    # r'^(java\.[\w.$]+(?:Exception|Error))\s(.*?)\n((?:\s+at .+\n?)*)', # rxjava
        # r'^(java\.[\w.$]+(?:Exception|Error))\s(.*?)\n((?:\s+at .+\n?)*)', # eclipse-collections
        r'^(java\.[\w.$]+(?:Exception|Error)):\s+(.*?)\n((?:[ \t]+at .+\n?)+)',
        re.MULTILINE
    )

    benchmark_method_to_err_msg = defaultdict()
    for log_file in logs:
        # if 'io.reactivex.rxjava3.processors.MulticastProcessorBenchmark.benchmarkThroughput.log' in str(log_file):
        #     import ipdb; ipdb.set_trace()
        content = log_file.read_text()
        if 'exception' in content.lower():
            maybe_error_benchmarks.append(log_file.with_suffix('').name)
            # Extract the full match blocks
            match = pattern.search(content)
            if match:
                exception_type = match.group(1)
                message = match.group(2)
                stack_trace = match.group(3)
                benchmark_method = log_file.relative_to(log_dir).with_suffix('')

                benchmark_method_to_err_msg[str(benchmark_method)] = f'Exception Type: {exception_type}\nStack Trace:\n{stack_trace}'
            else:
                print(f"No exception found: {log_file}")


    logging.info(f'{len(maybe_error_benchmarks)}\n {maybe_error_benchmarks}')
    for benchmark_method, err_msg in benchmark_method_to_err_msg.items():
        logging.info(f'{benchmark_method} -> {err_msg}')

    if args.branch == 'llm2jmh':
        with open(f'results/projects/{project}/generated/deepseek-chat/runtime-errors.json', 'w') as fd:
            json.dump(benchmark_method_to_err_msg, fd, indent=2)
    elif args.branch == 'llm2jmh-junit':
        with open(f'results/projects/{project}/generated/deepseek-chat-with-junit/runtime-errors.json', 'w') as fd:
            json.dump(benchmark_method_to_err_msg, fd, indent=2)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=False, help='rxjava,eclipse-collections,zipkin')
    parser.add_argument("--branch", default='llm2jmh', type=str, required=False, help='llm2jmh,llm2jmh-junit')
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
