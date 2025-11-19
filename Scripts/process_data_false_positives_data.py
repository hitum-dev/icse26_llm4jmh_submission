import platform

import os
import sys
import shutil
import subprocess
from typing import List, Tuple, Any, Optional, Literal
from pathlib import Path
import json
import re
from collections import Counter, defaultdict
import logging
import multiprocessing as mp
from multiprocessing import Pool
import numpy as np
import pandas as pd


logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)



def process_json_files(file_folder: Path, benches: List[str]):
    # Processes multiple JSON files from a zip archive and creates a boxplot of RSD values.
    all_rsd_values = []

    data = defaultdict(list)
    files = [x for x in file_folder.rglob('*.json') if not x.stem.startswith('00')]
    for file_path in files:
        # if '00-benchmark-methods.json' in str(file_path):
        #     continue
        # try:
        try:
            benchmark_results = json.loads(file_path.read_text())
        except json.JSONDecodeError:
            continue

        for benchmark_result in benchmark_results:
            raw_data = benchmark_result['primaryMetric']['rawData'][0]
            if len(raw_data) < 30:
                continue

            benchmark_name = benchmark_result['benchmark']
            params = benchmark_result.get("params", None)
            data['benchmark'].append(benchmark_name)
            # data['params'].append(params)

            for i, d in enumerate(raw_data):
                data[f'Iteration {i}'].append(d)

    df = pd.DataFrame(data)
    return df

def main(args):
    branch_mapping = {
        "rxjava": {
            "jmh": "JMH",
            "ju2jmh": "ju2jmh",
            "llm2jmh-gptoss-120b": "LLM4JMH",
        },
        "eclipse-collections": {
            "jmh-tests": "JMH",
            "ju2jmh": "ju2jmh",
            "ju2jmh.old1": "ju2jmh",
            "llm2jmh-gptoss-120b": "LLM4JMH",
        },
        "zipkin": {
            "benchmarks": "JMH",
            "ju2jmh": "ju2jmh",
            "llm2jmh-gptoss-120b": "LLM4JMH",
        },

    }
    # file_folder = Path(f"/Users/zxchen/Research/code/llm-pmf-exp/code/results/projects/{args.project}/benchmark/{args.branch}")
    file_folder = Path(f"/Users/zxchen/Research/code/llm-microbenchmark-selections/results/projects/{args.project}/benchmark/{args.branch}-fork_2")
    # if 'llm2jmh' in args.branch:
    #     file_folder = Path(f"/Users/zxchen/Research/code/llm-microbenchmark-selections/results/projects/{args.project}/benchmark/{args.branch}-fork_2")
    # else:
    #     file_folder = Path(f"/Users/zxchen/Research/code/llm-microbenchmark-selections/results/projects/{args.project}/benchmark/{args.branch}")
    common_method_cases_path = Path(f'/Users/zxchen/Research/code/llm-microbenchmark-selections/results/projects/{args.project}/coverage/llm2jmh-gptoss-120b_common_method_cases.json')
    common_method_cases = json.loads(common_method_cases_path.read_text())
    df = process_json_files(file_folder=file_folder, benches=common_method_cases[args.branch])
    mapped_branch = branch_mapping[args.project][args.branch]
    save_path = Path(f"./Data/RQ1-New/{args.project}-{mapped_branch}.csv")
    save_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(save_path)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=False)
    parser.add_argument("--branch", type=str, required=False)
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
