import json
from typing import List
from pathlib import Path
from xml.etree import ElementTree as ET
from collections import defaultdict
import pandas as pd

import logging

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def extract_related_benchmarks_by_source_method(files: List[Path]):
    src_method_to_benchmarks = defaultdict(list)
    for file in files:
        try:
            with open(file, 'r') as fd:
                method_to_line = json.load(fd)
            for method, line in method_to_line.items():
                benchmark_case = file.with_suffix('').name
                if benchmark_case not in src_method_to_benchmarks[(method, line)]:
                    src_method_to_benchmarks[(method, line)].append(benchmark_case)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {file}: {e}")
        except Exception as e:
            print(f"Unexpected error with file {file}: {e}")
    return src_method_to_benchmarks


def main(args):
    if args.branch is None or len(args.branch) < 2:
        logging.info("Please specify the branches to compare, at least 2 branches need to be specified")
        return

    branches = args.branch
    branch_info = {}
    common_methods = None
    for branch in branches:
        path = Path(f'results/projects/{args.project}/coverage/{branch}')
        json_files = sorted([x for x in path.glob('*.json') if not x.name.endswith('.detailed.json')])
        branch_info[branch] = extract_related_benchmarks_by_source_method(json_files)
        logging.info(f"{branch} covers {len(branch_info[branch].keys())} methods")
        if common_methods is None:
            common_methods = branch_info[branch].keys()
        else:
            common_methods = common_methods & branch_info[branch].keys()
        logging.info(f"number of common keys: {len(common_methods)}")

    common_methods = sorted(common_methods)

    data_list = []
    for method in common_methods:
        data = [method]
        for branch, src_method_to_benchmarks in branch_info.items():
            benchmarks = src_method_to_benchmarks[method]
            data.append(len(benchmarks))
        data_list.append(data)

    df = pd.DataFrame(data_list, columns=['method', *branch_info.keys()])
    df = df.sort_values(by=list(branch_info.keys()), ascending=False)

    filename = '_'.join(branches)
    filename = f'results/projects/{args.project}/coverage/common_methods_{filename}.csv'
    df.to_csv(filename, index=False)

    ################################################################################
    data_list = []
    for method in common_methods:
        data = [method]
        for branch, src_method_to_benchmarks in branch_info.items():
            benchmarks = src_method_to_benchmarks[method]
            data.append('|'.join(benchmarks))
        data_list.append(data)

    df = pd.DataFrame(data_list, columns=['method', *branch_info.keys()])
    filename = '_'.join(branches)
    filename = f'results/projects/{args.project}/coverage/common_methods_details_{filename}.csv'
    df.to_csv(filename, index=False)


if __name__ == '__main__':
    # python src/analysis_common_methods.py --project rxjava --branch jmh --branch llm2jmh --branch ju2jmh
    # python src/analysis_common_methods.py --project eclipse-collections --branch jmh --branch llm2jmh --branch ju2jmh
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=True, help='rxjava, eclipse-collections')
    parser.add_argument("--branch", action='append', help='rxjava: jmh,llm2jmh,ju2jmh; eclipse-collections: jmh-tests,llm2jmh,ju2jmh')
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
