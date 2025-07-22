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


def remove_java_comments(java_code: str) -> str:
    # Remove multi-line comments (/* ... */)
    java_code_no_multiline = re.sub(r'/\*[\s\S]*?\*/', '', java_code)

    # Remove single-line comments (// ...)
    java_code_no_comments = re.sub(r'//.*', '', java_code_no_multiline)

    return java_code_no_comments

def get_llm_prompt_by_src_code(src_code: str) -> str:
#     prompt = f""""
# Given the following Java source code, decide whether a JMH benchmark is needed. Only generate a benchmark if the method has non-trivial runtime behavior and is likely to benefit from throughput performance testing. Do not generate benchmarks for trivial methods like simple getters or constants.

# If a benchmark is needed:
# - Use JMH throughput mode and include warm-up and measurement phases.
# - Use realistic input sizes and setup methods if needed.
# - Include proper JMH annotations like @State, @Benchmark, and @Setup.
# - Embed best practices for reliable measurement.
# - Wrap the entire benchmark in triple backticks with no additional commentary.

# If no benchmark is needed, output SKIP and explain why.

# Source Code:
# {src_code}
# """

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
    prompt = f"""
Given the following Java source code, decide whether a JMH benchmark is needed.

Only generate a benchmark if the method has non-trivial runtime behavior and is likely to benefit from throughput performance testing. Do not generate benchmarks for trivial methods like simple getters or constants.

**However:**
- Treat any method that performs I/O, data copying, iteration, parsing, serialization, or other operations with variable runtime cost as non-trivial.
- Methods named 'read', 'write', 'process', 'parse', 'load', or similar should be treated as performance-critical candidates, even if they appear simple.
- Assume that performance tests for read operations are important to detect regressions.

**If a benchmark is needed:**
- Use JMH throughput mode and include warm-up and measurement phases.
- Use realistic input sizes and setup methods if needed.
- Include proper JMH annotations like @State, @Benchmark, and @Setup.
- Embed best practices for reliable measurement.
- Wrap the entire benchmark in triple backticks with no additional commentary.

**If no benchmark is needed**, output SKIP and briefly explain why.

**Examples:**
- A method like `public int read(byte[] b)` that reads data from a stream should have a benchmark.
- A simple getter like `getId()` should not.

Source Code:
{src_code}
"""
    return prompt


def generate_performance_tests(model: str, prompt: str) -> str:
    client = get_commercial_model(model)
    resp = prompt_commercial_model(client, model, prompt, image_id="")
    return resp

def generate_performance_tests_wrapper(args: Tuple[Any]):
    model, source_file, save_path = args
    if save_path.exists() and save_path.stat().st_size > 0:
        logging.info(f"{str(save_path)} is generated from model {model}, skip")
        return

    save_path.parent.mkdir(exist_ok=True, parents=True)
    with open(source_file, 'r') as fd:
        code = fd.read()

    pure_code = remove_java_comments(code)
    code_with_prompt = get_llm_prompt_by_src_code(pure_code)

    args = (model, code_with_prompt)
    logging.info(f"Will save the response into save_path: {save_path}")
    raw_resp = generate_performance_tests(*args)
    with open(save_path, 'w') as fd:
        fd.write(raw_resp)

def extract_code_in_backticks(unprocessed_code) -> Optional[str]:
    pattern = r"```.*?\n(.*?)```"
    codes = re.findall(pattern, unprocessed_code, re.DOTALL)
    if len(codes) == 0:
        return None
    return codes[0]

def save_code(save_path: Path) -> Literal[0, 1]:
    skip_cnt = 0
    with open(save_path, 'r') as fd:
        raw_code = fd.read()
    if 'SKIP' in raw_code:
        skip_cnt += 1

    only_code = extract_code_in_backticks(raw_code)
    if only_code is None:
        # logging.info(f"{str(source_file)} is no need to create jmh according to model {model}")
        return skip_cnt

    if 'repair-' in str(save_path):
        final_save_path = save_path.parent / save_path.name.split('.repair')[0]
    else:
        final_save_path = save_path.with_suffix('')

    with open(final_save_path, 'w') as fd:
        fd.write(only_code)

    return skip_cnt

def grok_gradlew_error_message(output: str) -> str:
    pattern = re.compile(
        r'> Task :compileJmhJava FAILED\n'       # Match the task failure line
        r'(?:.|\n)*?'                             # Lazily match any content
        r'\n\d+ error(s?)',                       # Match final error count line
        re.MULTILINE
    )

    match = pattern.search(output)
    if match:
        logging.info('############################################################')
        logging.error(match.group())
        logging.info('############################################################')
        return match.group()
    else:
        logging.info("No compile error block found.")
        return ''

def grok_maven_error_message(output: str) -> str:
    errors = [x for x in output.split('\n') if 'ERROR' in x or 'Compilation failure' in x]
    return '\n'.join(errors)


@patch_jpype
def main(args):
    root_branch = {
        'rxjava': 'jmh',
        'eclipse-collections': 'jmh-tests',
        'zipkin': 'benchmarks',
        'flink-17799': 'pre-FLINK-17799',
        'flink-16536': 'pre-FLINK-16536',
    }
    project = args.project
    mgr = get_manager(project, root_branch[project])
    src_dirs = mgr.src_dirs

    model = args.model
    strategy = args.strategy
    if strategy is not None:
        save_dir = Path(f'results/projects/{project}/generated/{model}-{strategy}')
    else:
        save_dir = Path(f'results/projects/{project}/generated/{model}')

    to_branch = args.to_branch
    repair_cnt = args.repair_cnt

    source_files = sorted([(src_dir, x.relative_to(src_dir)) for src_dir in src_dirs for x in src_dir.rglob('*.java')])
    pure_src_files = [str(x[1]) for x in source_files]
    counter = Counter(pure_src_files)
    if counter.most_common(1)[0][1] > 1:
        logging.error(f"Found duplicated file in {project}'s package, BUG?")
        import ipdb; ipdb.set_trace()

    logging.info(f"Total source files: {len(source_files)}")

    args_list = []
    for src_dir, source_file in source_files:
        _args = (model, src_dir / source_file, save_dir / f'{str(source_file)}.txt')
        args_list.append(_args)

    # args_list = args_list[:10]
    if args.parallel:
        with Pool(64) as pool:
            pool.map(generate_performance_tests_wrapper, args_list)
        pool.join()
    else:
        for _args in args_list:
            generate_performance_tests_wrapper(_args)

    # skip_cnt = 0
    # for source_file in source_files:
    #     save_path = save_dir / args.model / f'{str(source_file.relative_to(src_dir))}.txt'
    #     if save_path.exists():
    #         skip_cnt += save_code(save_path)
    #     save_path = save_dir / args.model / f'{str(source_file.relative_to(src_dir))}.repair-{0}.txt'
    #     if save_path.exists():
    #         skip_cnt += save_code(save_path)
    return
    skip_cnt = 0
    for src_dir, source_file in source_files:
        save_path = save_dir / f'{str(source_file)}.txt'
        if save_path.exists():
            skip_cnt += save_code(save_path)

        # NOTE: try normal generation first, then try repaired version
        save_path = save_dir / f'{str(source_file)}.repair-{repair_cnt}.txt'
        if save_path.exists():
            skip_cnt += save_code(save_path)

    java_files = sorted([x for x in save_dir.rglob('*.java')])
    logging.info(f"Analayze source code: {len(source_files)}, generated jmh files: {len(java_files)}, skip from response: {skip_cnt}")
    # NOTE: branch name is same as the jmh benchmarks directory, easy for branch switch and compilation
    subpackages = mgr.get_all_subpackages()
    # subpackages.append('org.openjdk.jmh.infra.Blackhole')

    # llm2jmh_dir = Path(f'{mgr.cwd}/{to_branch}/src/test/java')
    if args.project == 'eclipse-collections':
        llm2jmh_dir = Path(f'{mgr.cwd}/{to_branch}/src/main/java')
    elif args.project == 'rxjava':
        llm2jmh_dir = Path(f'{mgr.cwd}/{to_branch}/java')
    elif args.project == 'zipkin':
        llm2jmh_dir = Path(f'{mgr.cwd}/{to_branch}/src/main/java')
    # if llm2jmh_dir.exists():
    #     shutil.rmtree(str(llm2jmh_dir))
    elif args.project == 'flink-17799':
        llm2jmh_dir = Path(f'{mgr.cwd}/{to_branch}/src/main/java')

    elif args.project == 'flink-16536':
        llm2jmh_dir = Path(f'{mgr.cwd}/{to_branch}/src/main/java')

    valid_java_files = 0
    compiled_java_files = 0
    code_need_repair = {}

    import jpype
    from com.github.javaparser import StaticJavaParser
    from com.github.javaparser.ast.body import ClassOrInterfaceDeclaration
    # StaticJavaParser = jpype.JClass("com.github.javaparser.StaticJavaParser")
    # ClassOrInterfaceDeclaration = jpype.JClass("com.github.javaparser.ast.body.ClassOrInterfaceDeclaration")

    for java_file in java_files:
        with open(java_file, 'r') as fd:
            code = fd.read()
        try:
            cu = StaticJavaParser.parse(code)
        except Exception as ex:
            logging.info(f'{java_file} fail to parse')
            continue

        top_level_classes = [t.getNameAsString() for t in cu.getTypes() if isinstance(t, ClassOrInterfaceDeclaration) and not t.isInterface()]

        if len(top_level_classes) != 1:
            print(top_level_classes)
            # import ipdb; ipdb.set_trace()

        class_name = top_level_classes[0]

        for package in subpackages:
            try:
                cu.addImport(f'{package}.*')
            except Exception as ex:
                logging.error(f"Fail to add package {package}")
                # import ipdb; ipdb.set_trace()

        cu.addImport('org.openjdk.jmh.infra.Blackhole')

        dst_jmh_dir = (llm2jmh_dir / java_file.relative_to(save_dir)).parent
        dst_jmh_dir.mkdir(parents=True, exist_ok=True)
        dst_jmh_file = dst_jmh_dir / f'{class_name}.java'

        if dst_jmh_file.exists() and dst_jmh_file.stat().st_size > 0:
            compiled_java_files += 1
            valid_java_files += 1
            continue


        pkg_decl = cu.getPackageDeclaration()
        if pkg_decl.isPresent():
            cu.removePackageDeclaration()

        pkg_name = str(dst_jmh_dir.relative_to(llm2jmh_dir)).replace('/', '.')
        cu.setPackageDeclaration(pkg_name)

        code = str(cu.toString())

        with open(dst_jmh_file, 'w') as fd:
            fd.write(code)

        logging.info(f"Try compile with {dst_jmh_file}")
        try:
            mgr.compile(to_branch)
            compiled_java_files += 1
        except Exception as ex:
            if 'FAILED' in ex.output:
                # NOTE: rxjava compilation error message
                logging.error("------------------------------------------------------------")
                logging.error(f"Fail to compile the java code {str(dst_jmh_file)}, {ex.output}")
                err_msg = grok_gradlew_error_message(ex.output)
                code_need_repair[str(java_file)] = err_msg
                dst_jmh_file.unlink()
                logging.error("------------------------------------------------------------")
            elif 'ERROR' in ex.output:
                logging.error("------------------------------------------------------------")
                logging.error(f"Fail to compile the java code {str(dst_jmh_file)}, {ex.output}")
                err_msg = grok_maven_error_message(ex.output)
                code_need_repair[str(java_file)] = err_msg
                dst_jmh_file.unlink()
                logging.error("------------------------------------------------------------")
            else:
                logging.info(f"Compile java code successfully, {str(dst_jmh_file)}")
                import ipdb; ipdb.set_trace()
                dst_jmh_file.unlink()

        valid_java_files += 1

    with open(save_dir / f'repair-list-{repair_cnt}.json', 'w') as fd:
        json.dump(code_need_repair, fd, indent=2)

    logging.info(f"Analayze source code: {len(source_files)}, generated jmh files: {len(java_files)}, skip from respponse: {skip_cnt}, valid java file/compiled java file: {valid_java_files}/{compiled_java_files}")
    mgr.checkout_new_branch(to_branch)


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
