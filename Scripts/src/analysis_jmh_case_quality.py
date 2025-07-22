import os
import platform
from typing import List, Tuple, TypedDict
import sys
import shutil
import numpy as np
import pandas as pd
import argparse
import subprocess
import os
from pathlib import Path
import re
import json
from multiprocessing import Pool, Process, Value
from concurrent.futures import ProcessPoolExecutor
import logging
from multiprocessing import Manager
from utils_llm import get_commercial_model, prompt_commercial_model
import pandas as pd
from manager import get_manager
from utils import patch_jpype


logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class JmhQualityResponse(TypedDict):
    loc: int
    cyclomatic: int
    nesting_depth: int
    distinct_calls: int


def evaluate(code: str) -> JmhQualityResponse:
    from de.fraunhofer.fokus import JmhQualityAnalyzer

    try:
        method_to_features = JmhQualityAnalyzer.evaluate(code)
    except Exception as ex:
        return None

    return method_to_features

def evaluate_wrapper(_args):
    file, jmh_dir = _args
    logging.info(f"Processing file {str(file)}")
    class_name = str(file.relative_to(jmh_dir).with_suffix("")).replace('/', '.')
    code = file.read_text()
    method_to_features = evaluate(code)
    if method_to_features is None:
        return


@patch_jpype
def main(args):
    branch = args.branch
    mgr = get_manager(args.project, branch)
    jmh_dir = mgr.jmh_dir

    from de.fraunhofer.fokus import JmhQualityAnalyzer
    jmh_files = [x for x in jmh_dir.rglob('*.java')]
    saved_coverage_dir = mgr.save_coverage_dir
    trial_thrpts_files = [x for x in saved_coverage_dir.rglob('*.json')]
    saved_benchmark_dir = mgr.save_benchmark_dir
    real_thrpts_files = [x for x in saved_benchmark_dir.rglob('*.json')]

    features_records = []
    failed_to_process = 0
    failed_method_features = 0
    failed_benchmarks = 0
    missed_benchmarks = 0
    success_processed = 0
    for file in jmh_files:
        logging.info(f"Processing file {str(file)}")
        class_name = str(file.relative_to(jmh_dir).with_suffix("")).replace('/', '.')
        # logging.info(f"class_name: {class_name}")
        # if class_name != 'io.reactivex.rxjava3.parallel.ParallelFlowableBenchmark':
        #     continue

        code = file.read_text()
        try:
            method_to_features = JmhQualityAnalyzer.evaluate(code, [str(x) for x in mgr.src_dirs])
        except Exception as ex:
            logging.warning(f'Fail to process file: {str(file)}, exception: {str(ex)}')
            failed_to_process += 1
            continue

        if method_to_features is None:
            logging.warning(f'Fail to get method features: {str(file)}')
            failed_method_features += 1
            continue

        method_features = json.loads(str(method_to_features))
        for features in method_features:
            method = features['name']
            full_name = f'{class_name}.{method}'
            # if full_name != 'io.reactivex.rxjava3.parallel.ParallelFlowableBenchmark.parallelRunOn':
            #     continue

            # coverage_file = saved_coverage_dir / f'benchmark/{full_name}.json'
            # if not coverage_file.exists():
            #     logging.info(f"{full_name} coverage is missing")
            #     continue
            benchmark_file = saved_benchmark_dir / f'{full_name}.json'
            if not benchmark_file.exists():
                logging.warning(f"{full_name} benchmark is missing")
                missed_benchmarks += 1
                continue

            # dyn_results = json.loads(coverage_file.read_text())
            # features['dyn_thrpt_list'] = []
            # for dyn_result in dyn_results:
            #     features['dyn_thrpt_list'].append(dyn_result['primaryMetric']['score'])
            try:
                benchmark_results = json.loads(benchmark_file.read_text())
                features['rsd_list'] = []
                for benchmark_result in benchmark_results:
                    raw_data = np.array(benchmark_result['primaryMetric']['rawData'][0])
                    features['rsd_list'].append(np.std(raw_data) / np.mean(raw_data) * 100)
                features['name'] = full_name
                features_records.append(features)
                success_processed += 1
            except Exception as ex:
                logging.warning(f"Fail to parse benchmark results: {str(ex)}")
                failed_benchmarks += 1

    df = pd.DataFrame(features_records)

    df.to_json(f"{saved_coverage_dir}/features.jsonl", orient="records", lines=True)
    logging.info("Analyze features of generated jmh cases successfully.")
    logging.info(f"total files: {len(real_thrpts_files)}, success_processed: {success_processed}, failed_to_process: {failed_to_process}, failed_method_features: {failed_method_features}, failed_benchmarks: {failed_benchmarks}, missing_benchmarks: {missed_benchmarks}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=True, help='rxjava, eclipse-collections, zipkin')
    parser.add_argument("--branch", type=str, default='jmh')
    args = parser.parse_args()
    main(args)
