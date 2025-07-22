import pandas as pd
import numpy as np
from collections import defaultdict
from pathlib import Path
import json
from typing import List

import logging


logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def extract_common_stats_from_jmh_files(project: str, branch: str, bug: str, injected_method: str, injected_line: int):
    normal_dir = Path(f'./results/projects/{project}/benchmark/{branch}')
    buggy_dir = Path(f'./results/projects/{project}/benchmark/{branch}_{bug}_{injected_method}_{injected_line}')

    if project == 'rxjava':
        branches = ['jmh', 'ju2jmh', 'llm2jmh']
    elif project == 'eclipse-collections':
        branches = ['jmh-tests', 'ju2jmh', 'llm2jmh']
    elif project == 'zipkin':
        branches = ['benchmarks', 'ju2jmh', 'llm2jmh']
    df = pd.read_csv(f'./results/projects/{project}/coverage/common_methods_details_{"_".join(branches)}.csv')

    jmh_methods = []
    for i, row in df.iterrows():
        method, line = eval(row['method'])
        method = method.replace('$', '-')
        if method == injected_method and line == injected_line:
            jmh_methods = row[branch].split('|')
            break

    print(f'Number of jmh methods involved: {len(jmh_methods)}, injected method: {project}/{injected_method}')

    selected_normal_stats = []
    selected_buggy_stats = []
    for jmh_method in jmh_methods:
        normal_file = normal_dir / f"{jmh_method}.json"
        buggy_file = buggy_dir / f"{jmh_method}.json"
        # print(f'buggy_files: {str(buggy_file)}')
        if buggy_file.exists():
            try:
                with open(buggy_file, 'r') as fd:
                    buggy_benchmarks = json.load(fd)

                with open(normal_file, 'r') as fd:
                    normal_benchmarks = json.load(fd)

                if len(buggy_benchmarks) != len(normal_benchmarks):
                    print(f"{jmh_method} is malformed")
                    continue

                for normal, buggy in zip(normal_benchmarks, buggy_benchmarks):
                    if 'params' in normal:
                        normal_params = normal['params']
                        buggy_parmas = buggy['params']
                        if buggy_parmas != normal_params:
                            print(f'{jmh_method} params are mismatched')
                            continue
                    # if buggy['primaryMetric']['score'] > normal['primaryMetric']['score']:
                    #     print(f"BUGGY method {jmh_method} has higher score than normal: {buggy['primaryMetric']['score']} > {normal['primaryMetric']['score']}")
                    #     continue

                    selected_buggy_stats.append(buggy)
                    selected_normal_stats.append(normal)
            except json.JSONDecodeError as e:
                pass
            except Exception as e:
                print(f"Unexpected error with file {normal_file}: {e}")

    normal_thrpts_list = [x['primaryMetric']['rawData'][-1] for x in selected_normal_stats]
    buggy_thrpts_list = [x['primaryMetric']['rawData'][-1] for x in selected_buggy_stats]
    print(f"Collect {len(normal_thrpts_list)} valid cases")
    return normal_thrpts_list, buggy_thrpts_list

# JMH Ratio of means confidence interval (bootstrap method)
def bootstrap_ci(before, after, iters=10000):
    ratios = []
    for _ in range(iters):
        b = np.random.choice(before, len(before), replace=True)
        a = np.random.choice(after, len(after), replace=True)
        ratios.append(np.mean(a) / np.mean(b))
    # RCI is the 0.5% and 99.5% percentiles of the bootstrap ratios
    return np.percentile(ratios, [0.5, 99.5])


def get_bug_sizes(project: str, branch: str, bug: str, injected_method: str, injected_line: int) -> List[float]:
    normal_thrpts_list, buggy_thrpts_list = extract_common_stats_from_jmh_files(project, branch, bug, injected_method, injected_line)
    bug_sizes = []
    for normal_thrpts, buggy_thrpts in zip(normal_thrpts_list, buggy_thrpts_list):
        lower, upper = bootstrap_ci(normal_thrpts, buggy_thrpts)
        bug_size = (1 - upper)
        # bug_sizes.append({'bug_size': bug_size, 'normal': np.mean(normal_thrpts), 'buggy': np.mean(buggy_thrpts), 'injected_method': injected_method})
        bug_sizes.append(bug_size)
    return bug_sizes


def main(args):
    project = args.project
    # branch = 'llm2jmh'
    bug = args.bug
    # injected_method = 'io.reactivex.rxjava3.internal.util.BackpressureHelper.add'
    save_path = f'results/projects/{project}/benchmark/bug-{bug}.json'
    # injected_line = 51

    if project == 'rxjava':
        method_line_list = [
            'io.reactivex.rxjava3.core.Flowable.bufferSize_255',
            'io.reactivex.rxjava3.core.Observable.just_2649',
            'io.reactivex.rxjava3.internal.functions.ObjectHelper.verifyPositive_51',
            'io.reactivex.rxjava3.internal.operators.flowable.FlowableFromArray.subscribeActual_35',
            'io.reactivex.rxjava3.internal.operators.mixed.MaybeFlatMapObservable-FlatMapObserver.onNext_69',
            'io.reactivex.rxjava3.internal.operators.observable.ObservableFromArray-FromArrayDisposable.isDisposed_96',
            'io.reactivex.rxjava3.internal.util.BackpressureHelper.add_69',
            'io.reactivex.rxjava3.internal.util.ExceptionHelper-Termination.fillInStackTrace_143',
            'io.reactivex.rxjava3.internal.util.OpenHashSet.add_58',
            'io.reactivex.rxjava3.core.Flowable.bufferSize_255',
            'io.reactivex.rxjava3.core.Maybe.empty_914',
            'io.reactivex.rxjava3.core.Maybe.just_1319',
            'io.reactivex.rxjava3.core.Observable.fromArray_1925',
            'io.reactivex.rxjava3.core.Observable.just_2649',
            'io.reactivex.rxjava3.core.Scheduler.scheduleDirect_234',
            'io.reactivex.rxjava3.core.Single.just_1243',
            'io.reactivex.rxjava3.internal.disposables.DisposableHelper.replace_99',
            'io.reactivex.rxjava3.internal.disposables.DisposableHelper.setOnce_78',
            'io.reactivex.rxjava3.internal.functions.ObjectHelper.verifyPositive_51',
            'io.reactivex.rxjava3.internal.operators.flowable.FlowableFromArray.subscribeActual_35',
            'io.reactivex.rxjava3.internal.operators.flowable.FlowableJust.get_39 ',
            'io.reactivex.rxjava3.internal.operators.mixed.MaybeFlatMapObservable-FlatMapObserver.onNext_69',
            'io.reactivex.rxjava3.internal.operators.observable.ObservableFlatMap-MergeObserver.onSubscribe_103',
            'io.reactivex.rxjava3.internal.operators.observable.ObservableFromArray-FromArrayDisposable.isDisposed_96',
            'io.reactivex.rxjava3.internal.operators.observable.ObservableFromArray.subscribeActual_30',
            'io.reactivex.rxjava3.internal.operators.observable.ObservableScalarXMap.scalarXMap_115',
            'io.reactivex.rxjava3.internal.operators.single.SingleFlatMapPublisher-SingleFlatMapPublisherObserver.onComplete_112',
            'io.reactivex.rxjava3.internal.schedulers.SingleScheduler.createExecutor_68',
            'io.reactivex.rxjava3.internal.subscriptions.SubscriptionHelper.validate_80',
            'io.reactivex.rxjava3.internal.util.BackpressureHelper.add_69',
            'io.reactivex.rxjava3.internal.util.ExceptionHelper-Termination.fillInStackTrace_143',
            'io.reactivex.rxjava3.internal.util.OpenHashSet.add_58',
            'io.reactivex.rxjava3.plugins.RxJavaPlugins.onAssembly_1046',
            'io.reactivex.rxjava3.plugins.RxJavaPlugins.onSubscribe_931',
            'io.reactivex.rxjava3.schedulers.Schedulers.computation_142',
        ]
        branches = ['jmh', 'ju2jmh', 'llm2jmh']
    elif project == 'eclipse-collections':
        method_line_list = [
            # 'org.eclipse.collections.api.list.MutableList.toImmutable_383',
            # 'org.eclipse.collections.impl.AbstractRichIterable.forEach_561',
            # 'org.eclipse.collections.impl.list.IntervalUtils.checkArguments_26',
            # 'org.eclipse.collections.impl.list.mutable.FastList.batchForEach_239',
            # 'org.eclipse.collections.impl.set.mutable.UnifiedSet.toSentinelIfNull_2335',
            # 'org.eclipse.collections.impl.utility.internal.InternalArrayIterate.noneSatisfy_796',
            'org.eclipse.collections.api.factory.ServiceLoaderUtils.loadServiceClass_317',
            'org.eclipse.collections.api.list.MutableList.toImmutable_383',
            'org.eclipse.collections.impl.AbstractRichIterable.forEach_561',
            'org.eclipse.collections.impl.block.factory.primitive.IntToIntFunctions-IncrementIntToIntFunction.valueOf_53',
            'org.eclipse.collections.impl.block.procedure.CollectionAddProcedure.on_33',
            'org.eclipse.collections.impl.collection.mutable.AbstractMutableCollection.addAll_199',
            'org.eclipse.collections.impl.list.Interval.size_769',
            'org.eclipse.collections.impl.list.IntervalUtils.checkArguments_26',
            'org.eclipse.collections.impl.list.IntervalUtils.valueAtIndex_88',
            'org.eclipse.collections.impl.list.mutable.FastList.add_1069',
            'org.eclipse.collections.impl.list.mutable.FastList.batchForEach_239',
            'org.eclipse.collections.impl.list.mutable.FastList.copyItemsWithNewCapacity_465',
            'org.eclipse.collections.impl.list.mutable.FastList.get_1054',
            'org.eclipse.collections.impl.list.mutable.FastList.newListWith_186',
            'org.eclipse.collections.impl.list.mutable.FastList.newList_170',
            'org.eclipse.collections.impl.list.mutable.FastList.newWithNValues_196',
            'org.eclipse.collections.impl.list.mutable.FastList.size_1229',
            'org.eclipse.collections.impl.parallel.BatchIterableProcedureFJTask.run_46',
            'org.eclipse.collections.impl.partition.list.PartitionFastList.getSelected_26',
            'org.eclipse.collections.impl.set.mutable.UnifiedSet.getTable_205',
            'org.eclipse.collections.impl.set.mutable.UnifiedSet.index_219',
            'org.eclipse.collections.impl.set.mutable.UnifiedSet.nonNullTableObjectEquals_2344',
            'org.eclipse.collections.impl.set.mutable.UnifiedSet.toSentinelIfNull_2335',
            'org.eclipse.collections.impl.utility.Iterate.forEachWith_157',
            'org.eclipse.collections.impl.utility.Iterate.isEmpty_1785',
            'org.eclipse.collections.impl.utility.internal.InternalArrayIterate.batchForEach_172',
            'org.eclipse.collections.impl.utility.internal.InternalArrayIterate.noneSatisfy_796',
        ]
        branches = ['jmh-tests', 'ju2jmh', 'llm2jmh']
    elif project == 'zipkin':
        method_line_list = [
            # 'zipkin2.internal.ThriftCodec.readListLength_105',
            # 'zipkin2.Span.toLowerHex_667',
            # 'zipkin2.Endpoint-Builder.ip_227',
            # 'zipkin2.v1.V1Span-Builder.duration_236',
            # 'zipkin2.internal.WriteBuffer.writeAscii_147',
            # 'zipkin2.Endpoint.ipv6_71',
            # 'zipkin2.internal.JsonCodec-JsonReader.endArray_63',
            # 'zipkin2.internal.WriteBuffer.writeLongLe_184',
            # 'zipkin2.Span-Builder.duration_503',
            # 'zipkin2.Endpoint.notHex_366',
            'zipkin2.Endpoint-Builder.ip_227',
            'zipkin2.Endpoint.ipv6_71',
            'zipkin2.Endpoint.notHex_366',
            'zipkin2.Span-Builder.clear_297',
            'zipkin2.Span-Builder.duration_503',
            'zipkin2.Span.duration_503',
            'zipkin2.Span.toLowerHex_667',
            'zipkin2.internal.JsonCodec-JsonReader.endArray_63',
            'zipkin2.internal.ReadBuffer.readUtf8_281',
            'zipkin2.internal.ThriftCodec.readListLength_105',
            'zipkin2.internal.ThriftField.isEqualTo_52',
            'zipkin2.internal.WriteBuffer.writeAscii_147',
            'zipkin2.internal.WriteBuffer.writeLongLe_184',
            'zipkin2.internal.WriteBuffer.writeVarint_167',
            'zipkin2.v1.V1Span-Builder.duration_236',
            'zipkin2.v1.V1SpanConverter.processAnnotations_62',


            'zipkin2.Endpoint-Builder.build_288',
            'zipkin2.Endpoint-Builder.ip_227',
            'zipkin2.Endpoint.getIpv4Bytes_626',
            'zipkin2.Endpoint.ipv6_71',
            'zipkin2.Endpoint.newBuilder_107',
            'zipkin2.Endpoint.notHex_366',
            'zipkin2.Span-Builder.build_596',
            'zipkin2.Span-Builder.clear_297',
            'zipkin2.Span-Builder.duration_503',
            'zipkin2.Span-Builder.id_464',
            'zipkin2.Span-Builder.name_483',
            'zipkin2.Span.duration_503',
            'zipkin2.Span.shared_263',
            'zipkin2.Span.toLowerHex_667',
            'zipkin2.Span.writeHexByte_685',
            'zipkin2.internal.HexCodec.lowerHexToUnsignedLong_41',
            'zipkin2.internal.JsonCodec-JsonReader.endArray_63',
            'zipkin2.internal.JsonCodec-JsonReader.endObject_71',
            'zipkin2.internal.JsonCodec.read_125',
            'zipkin2.internal.ReadBuffer-Array.available_245',
            'zipkin2.internal.ReadBuffer.readUtf8_281',
            'zipkin2.internal.ReadBuffer.require_380',
            'zipkin2.internal.ReadBuffer.wrapUnsafe_28',
            'zipkin2.internal.ReadBuffer.wrap_42',
            'zipkin2.internal.RecyclableBuffers.shortStringBuffer_32',
            'zipkin2.internal.ThriftCodec.readListLength_105',
            'zipkin2.internal.ThriftField.isEqualTo_52',
            'zipkin2.internal.WriteBuffer.asciiSizeInBytes_241',
            'zipkin2.internal.WriteBuffer.wrap_35',
            'zipkin2.internal.WriteBuffer.writeAscii_147',
            'zipkin2.internal.WriteBuffer.writeByte_47',
            'zipkin2.internal.WriteBuffer.writeLongLe_184',
            'zipkin2.internal.WriteBuffer.writeVarint_167',
            'zipkin2.v1.V1BinaryAnnotation.compareTo_118',
            'zipkin2.v1.V1Span-Builder.duration_236',
            'zipkin2.v1.V1Span-Builder.id_205',
            'zipkin2.v1.V1Span-Builder.name_224',
            'zipkin2.v1.V1Span.newBuilder_134',
            'zipkin2.v1.V1SpanConverter.hasSameServiceName_313',
            'zipkin2.v1.V1SpanConverter.processAnnotations_62',
            'zipkin2.v1.V2SpanConverter.convert_37',
        ]

        branches = ['benchmarks', 'ju2jmh', 'llm2jmh']

    df = pd.read_csv(f'./results/projects/{project}/coverage/common_methods_details_{"_".join(branches)}.csv')

    total_cases = defaultdict(list)

    for branch in branches:
        for method_line in method_line_list:
            for i, row in df.iterrows():
                injected_method, injected_line = method_line.split('_')
                injected_line = int(injected_line)

                method, line = eval(row['method'])
                method = method.replace('$', '-')
                if method == injected_method and line == injected_line:
                    # total_cases[branch] += row[branch]
                    jmh_methods = row[branch].split('|')
                    total_cases[branch].extend(jmh_methods)
                    break

    # print(total_cases)
    for branch, cases in total_cases.items():
        print(f'{branch}: {len(cases)}, {len(set(cases))}')

    try:
        with open(save_path, 'r') as fp:
            method_to_branch_to_bug_sizes = json.load(fp)
    except Exception as ex:
        method_to_branch_to_bug_sizes = {}

    for method_line in method_line_list:
        injected_method, injected_line = method_line.split('_')

        if method_line not in method_to_branch_to_bug_sizes:
            method_to_branch_to_bug_sizes[method_line] = {}

        for branch in branches:
            if branch in method_to_branch_to_bug_sizes[method_line]:
                continue
            print(f'injected_method: {injected_method}, injected_line: {injected_line}')
            bug_sizes = get_bug_sizes(project, branch, bug, injected_method, int(injected_line))
            method_to_branch_to_bug_sizes[method_line][branch] = bug_sizes

            with open(save_path, 'w') as fp:
                json.dump(method_to_branch_to_bug_sizes, fp, indent=2)

    with open(save_path, 'w') as fp:
        json.dump(method_to_branch_to_bug_sizes, fp, indent=2)

    # method_to_branch_to_thrpt = {}
    # for method, branch_to_bug_sizes in method_to_branch_to_bug_sizes.items():
    #     method_to_branch_to_thrpt[method] = {}
    #     for branch, bug_sizes in branch_to_bug_sizes.items():
    #         method_to_branch_to_thrpt[method][branch] = {'max': float('-inf'), 'min': float('inf')}
    #         for bug_size in bug_sizes:
    #             bs = bug_size['bug_size'] * 100
    #             normal = bug_size['normal']
    #             buggy = bug_size['buggy']
    #             if bs >= 1:
    #                 method_to_branch_to_thrpt[method][branch]['max'] = max(method_to_branch_to_thrpt[method][branch]['max'], buggy)
    #                 method_to_branch_to_thrpt[method][branch]['min'] = min(method_to_branch_to_thrpt[method][branch]['min'], buggy)

    # branch_to_max_times = defaultdict(list)
    # branch_to_min_times = defaultdict(list)

    # for method, branch_to_thrpt in method_to_branch_to_thrpt.items():
    #     for branch, thrpt in branch_to_thrpt.items():
    #         max_thrpt = thrpt['max']
    #         min_thrpt = thrpt['min']
    #         # logging.info(f'min time: {branch} {1.0/max_thrpt*1000000:.3f} -> {method}')
    #         # logging.info(f'max time: {branch} {1.0/min_thrpt*1000000:.3f} -> {method}')
    #         branch_to_max_times[branch].append(1/min_thrpt)
    #         branch_to_min_times[branch].append(1/max_thrpt)

    # for branch, max_times in branch_to_max_times.items():
    #     max_time = np.mean(max_times)

    #     logging.info(f"max_time ({branch}): {max_time}")
    # for branch, min_times in branch_to_min_times.items():
    #     min_time = np.mean(min_times)
    #     logging.info(f"min_time ({branch}): {min_time}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=True, help='rxjava, eclipse-collections')
    parser.add_argument("--bug", type=str, default='HWO', help='HWO,STS,PTW')
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
