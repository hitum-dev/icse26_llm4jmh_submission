import random
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

def main(args):
    common_methods_path = Path(args.common_methods_path)
    df = pd.read_csv(str(common_methods_path))
    # method_and_line_list = [eval(x) for x in df['method'].to_list()]

    # for method, line in method_and_line_list:
    #     if method not in methods:
    #         methods.append(method)
    #     else:
    #         logging.info(f'Found duplicated method {method}')
    jmh_key = None
    if 'eclipse-collections' in str(common_methods_path):
        jmh_key = 'jmh-tests'
    elif 'rxjava' in str(common_methods_path):
        jmh_key = 'jmh'
    elif 'zipkin' in str(common_methods_path):
        jmh_key = 'benchmarks'

    # max_value = int(df[jmh_key].max())
    max_value = int(df['llm2jmh'].max())

    total_bin = 50
    bin_step = max_value // total_bin + 1

    bins = [[] for _ in range(total_bin)]

    for i, row in df.iterrows():
        method, line = eval(row['method'])
        jmh = row[jmh_key]
        ju2jmh = row['ju2jmh']
        llm2jmh = row['llm2jmh']
        # bins[jmh // bin_step].append((method, line, jmh, ju2jmh, llm2jmh))
        bins[llm2jmh // bin_step].append((method, line, jmh, ju2jmh, llm2jmh))


    # stratified sampling
    random.seed(41)
    selected_methods = []
    for i, bin in enumerate(bins):
        print(i, bin)
        if len(bin) > 0:
            selected = random.choice(bin)
            selected_methods.append(selected)

    for method in selected_methods:
        print(method)

    selected_methods_path = common_methods_path.parent / 'selected_methods.json'
    with open(selected_methods_path, 'w') as fd:
        json.dump(selected_methods, fd, indent=2)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--common_methods_path", type=str, required=False)

    args = parser.parse_args()

    main(args)
