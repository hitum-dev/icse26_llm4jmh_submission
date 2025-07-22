import time
import pandas as pd
import numpy as np
from collections import defaultdict
from pathlib import Path
import json
from typing import List
from scipy.stats import bootstrap
import logging
import numpy as np
import pandas as pd


logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)



def get_rciw_list(project: str, branch: str, bug: str, injected_method: str, injected_line: int) -> List[float]:
    rciw_list = []
    normal_dir = Path(f'./results/projects/{project}/benchmark/{branch}')

    for jmh_file in normal_dir.rglob("*.json"):
        try:
            normal_benchmarks = json.loads(jmh_file.read_bytes())
            for x in normal_benchmarks:
                raw_data = x['primaryMetric']['rawData'][-1]

                rciw_seq = []

                for index in range(2, len(raw_data)+1, 1):
                    res = bootstrap((raw_data[:index],), np.mean, confidence_level=0.99, n_resamples=10000, method='percentile')
                    L, U = res.confidence_interval.low, res.confidence_interval.high
                    mean = np.mean(raw_data[:index])
                    rciw = (U - L) / mean
                    rciw_seq.append(rciw)

                rciw_list.append(rciw_seq)
        except Exception as ex:
            pass
    return rciw_list

#
def main(args):
    project = args.project
    # branch = 'llm2jmh'
    bug = args.bug

    save_path = f'results/projects/{project}/benchmark/rciw-{bug}.json'

    if project == 'rxjava':
        branches = ['jmh', 'ju2jmh', 'llm2jmh']
    elif project == 'eclipse-collections':
        branches = ['jmh-tests', 'ju2jmh', 'llm2jmh']
    elif project == 'zipkin':
        branches = ['benchmarks', 'ju2jmh', 'llm2jmh']

    # try:
    #     with open(save_path, 'r') as fp:
    #         branch_to_rciw_list = json.load(fp)
    # except Exception as ex:
    #     branch_to_rciw_list = {}

    branch_to_rciw_list = {}

    for branch in branches:
        # if branch in branch_to_rciw_list:
        #     continue
        ci_list = get_rciw_list(project, branch, bug, None, None)
        branch_to_rciw_list[branch] = ci_list
        with open(save_path, 'w') as fp:
            json.dump(branch_to_rciw_list, fp)

    with open(save_path, 'w') as fp:
        json.dump(branch_to_rciw_list, fp)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=True, help='rxjava, eclipse-collections')
    parser.add_argument("--bug", type=str, default='HWO', help='HWO,STS,PTW')
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
