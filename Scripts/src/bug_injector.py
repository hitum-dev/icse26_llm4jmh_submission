import os
import platform
from typing import List, Tuple, TypedDict
import sys
import shutil
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


class MutationResponse(TypedDict):
    mutated_code: str
    injected_bugs: int


def mutate(code: str, method: str, line: int, bug: str, max_injected_bugs: int = 1) -> MutationResponse:
    from de.fraunhofer.fokus import PerformanceMutator
    result = PerformanceMutator.mutate(code, method, line, bug.upper(), max_injected_bugs)
    res = json.loads(str(result))
    return res


# def extract_java_info(source_code: str):
#     JavaParser = jpype.JClass("com.github.javaparser.JavaParser")
#     ClassOrInterfaceDeclaration = jpype.JClass("com.github.javaparser.ast.body.ClassOrInterfaceDeclaration")
#     ImportDeclaration = jpype.JClass("com.github.javaparser.ast.ImportDeclaration")
#     PackageDeclaration = jpype.JClass("com.github.javaparser.ast.PackageDeclaration")

#     parser = JavaParser()
#     result = parser.parse(source_code)

#     if not (result.isSuccessful() and result.getResult().isPresent()):
#         raise RuntimeError("JavaParser failed to parse source")

#     cu = result.getResult().get()

#     # --- Extract package name ---
#     package_name = None
#     if cu.getPackageDeclaration().isPresent():
#         package_decl = cu.getPackageDeclaration().get()
#         package_name = package_decl.getNameAsString()

#     # --- Extract imports ---
#     import_list = []
#     imports = cu.getImports()
#     for i in range(imports.size()):
#         imp = imports.get(i)
#         # imp.toString() returns import statement including newline, strip it
#         import_list.append(str(imp.toString()).strip())

#     # --- Extract methods grouped by class ---
#     methods_by_class = {}

#     def recurse_class(cls, prefix=None):
#         class_name = cls.getNameAsString()
#         full_name = f"{prefix}.{class_name}" if prefix else class_name

#         # Extract methods directly declared in this class
#         methods = cls.getMethods()
#         methods_list = []
#         for i in range(methods.size()):
#             m = methods.get(i)
#             methods_list.append(str(m.toString()))

#         methods_by_class[full_name] = methods_list

#         # Find inner classes declared as members
#         members = cls.getMembers()
#         for i in range(members.size()):
#             member = members.get(i)
#             if member.getClass().getSimpleName() == "ClassOrInterfaceDeclaration":
#                 recurse_class(member, prefix=full_name)

#     # Start from top-level classes (parent node is CompilationUnit)
#     classes = cu.findAll(ClassOrInterfaceDeclaration.class_)
#     for i in range(classes.size()):
#         cls = classes.get(i)
#         parent = cls.getParentNode()
#         if parent.isPresent() and parent.get().getClass().getSimpleName() == "CompilationUnit":
#             recurse_class(cls)

#     return {
#         "package": package_name,
#         "imports": import_list,
#         "methods_by_class": methods_by_class,
#     }


# def select(method_and_line_list: List[Tuple[str, int]]) -> Tuple[str, int]:
#     return method_and_line_list[0]


def debug():
    # 5. Sample code to mutate
    # PerformanceMutator = jpype.JClass("de.fraunhofer.fokus.PerformanceMutator")
    # PerformanceMutator = jpype.JClass("de.fraunhofer.fokus.PerformanceMutator")
    from de.fraunhofer.fokus import PerformanceMutator
    method_code = """
public long compute(List<Integer> nums, long total) {
    StringBuilder sb = new StringBuilder();
    for (int i : nums) {
        if (i < 10) {
            sb.append(i);
        }
    }
    {
       StringBuilder sb = new StringBuilder();
    }
    {
       StringBuilder sc = new StringBuilder();
    }
    StringBuilder cb = new StringBuilder();
    return total;
}

public int compute(int num) {
   return num;
}
public long compute(long num) {
   return num;
}
public byte compute(byte num) {
   return num;
}
public float compute(float num) {
   return num;
}
public double compute(double num) {
   return num;
}
public boolean compute(boolean num) {
   return num;
}
"""

    wrapped_code = f"""import java.util.*;
public class Dummy {{
    {method_code}
}}
"""
    print('-------------------- Original Code --------------------')
    print(wrapped_code)
    print('-------------------- Mutate Method hello_world:4 (No such method)--------------------')
    result = PerformanceMutator.mutate(wrapped_code, "hello_world", 4, "HWO")
    print(result)
    res = json.loads(str(result))
    mutated_code = res['mutated_code']
    injected_bugs = res['injected_bugs']
    print(mutated_code)
    print(f"> injected bugs: {injected_bugs}")
    print('-------------------- Mutate Method compute:2 (Incorrect line position) --------------------')
    result = PerformanceMutator.mutate(wrapped_code, "compute", 2, "HWO")
    print(result)
    res = json.loads(str(result))
    mutated_code = res['mutated_code']
    injected_bugs = res['injected_bugs']
    print(mutated_code)
    print(f"> injected bugs: {injected_bugs}")
    print('-------------------- Mutate Method compute:4 (Should be result, HWO)--------------------')
    result = PerformanceMutator.mutate(wrapped_code, "compute", 4, "HWO")
    res = json.loads(str(result))
    mutated_code = res['mutated_code']
    injected_bugs = res['injected_bugs']
    print(mutated_code)
    print(f"> injected bugs: {injected_bugs}")
    print('-------------------- Mutate Method compute:4 (Should be result, STS) --------------------')
    result = PerformanceMutator.mutate(wrapped_code, "compute", 4, "STS")
    res = json.loads(str(result))
    mutated_code = res['mutated_code']
    injected_bugs = res['injected_bugs']
    print(mutated_code)
    print(f"> injected bugs: {injected_bugs}")
    print('-------------------- Mutate Method compute:4 (Should be result, STS, 2) --------------------')
    result = PerformanceMutator.mutate(wrapped_code, "compute", 4, "STS", 2)
    res = json.loads(str(result))
    mutated_code = res['mutated_code']
    injected_bugs = res['injected_bugs']
    print(mutated_code)
    print(f"> injected bugs: {injected_bugs}")
    print('-------------------- Mutate Method compute:4 (Should be result, STS, 3) --------------------')
    result = PerformanceMutator.mutate(wrapped_code, "compute", 4, "STS", 3)
    res = json.loads(str(result))
    mutated_code = res['mutated_code']
    injected_bugs = res['injected_bugs']
    print(mutated_code)
    print(f"> injected bugs: {injected_bugs}")
    print('-------------------- Mutate Method compute:4 (Should be result, PTW) --------------------')
    result = PerformanceMutator.mutate(wrapped_code, "compute", 4, "PTW")
    res = json.loads(str(result))
    mutated_code = res['mutated_code']
    injected_bugs = res['injected_bugs']
    print(mutated_code)
    print(f"> injected bugs: {injected_bugs}")

    # print('-------------------- Mutate Method compute:4 (Should be result, PTW, int) --------------------')
    # result = PerformanceMutator.mutate(wrapped_code, "compute", 16, "PTW")
    # print(result)
    # res = json.loads(str(result))
    # mutated_code = res['mutated_code']
    # injected_bugs = res['injected_bugs']
    # print(mutated_code)
    # print(f"> injected bugs: {injected_bugs}")

    # print('-------------------- Mutate Method compute:4 (Should be result, PTW, long) --------------------')
    # result = PerformanceMutator.mutate(wrapped_code, "compute", 19, "PTW")
    # print(result)
    # res = json.loads(str(result))
    # mutated_code = res['mutated_code']
    # injected_bugs = res['injected_bugs']
    # print(mutated_code)
    # print(f"> injected bugs: {injected_bugs}")
    # print('-------------------- Mutate Method compute:4 (Should be result, PTW, byte) --------------------')
    # result = PerformanceMutator.mutate(wrapped_code, "compute", 22, "PTW")
    # print(result)
    # res = json.loads(str(result))
    # mutated_code = res['mutated_code']
    # injected_bugs = res['injected_bugs']
    # print(mutated_code)
    # print(f"> injected bugs: {injected_bugs}")
    # print('-------------------- Mutate Method compute:4 (Should be result, PTW, float) --------------------')
    # result = PerformanceMutator.mutate(wrapped_code, "compute", 25, "PTW")
    # print(result)
    # res = json.loads(str(result))
    # mutated_code = res['mutated_code']
    # injected_bugs = res['injected_bugs']
    # print(mutated_code)
    # print(f"> injected bugs: {injected_bugs}")
    # print('-------------------- Mutate Method compute:4 (Should be result, PTW, double) --------------------')
    # result = PerformanceMutator.mutate(wrapped_code, "compute", 28, "PTW")
    # print(result)
    # res = json.loads(str(result))
    # mutated_code = res['mutated_code']
    # injected_bugs = res['injected_bugs']
    # print(mutated_code)
    # print(f"> injected bugs: {injected_bugs}")
    # print('-------------------- Mutate Method compute:4 (Should be result, PTW, boolean) --------------------')
    # result = PerformanceMutator.mutate(wrapped_code, "compute", 31, "PTW")
    # print(result)
    # res = json.loads(str(result))
    # mutated_code = res['mutated_code']
    # injected_bugs = res['injected_bugs']
    # print(mutated_code)
    # print(f"> injected bugs: {injected_bugs}")


@patch_jpype
def main(args):
    if args.debug:
        return debug()

    # common_methods_path = Path(args.common_methods_path)
    # df = pd.read_csv(str(common_methods_path))
    # method_and_line_list = [eval(x) for x in df['method'].to_list()]

    # for method_and_line in method_and_line_list:
    project = args.project
    with open(f'results/projects/{project}/coverage/selected_methods.json', 'r') as fd:
        selected_methods = json.load(fd)

    from_branch = args.from_branch
    for selected_method in selected_methods:
        mgr = get_manager(project, from_branch)
        # method, line = args.method, args.line
        method, line = selected_method[0], selected_method[1]
        if '$' in method:
            method = method.replace('$', '-')

        to_branch = f'{from_branch}_{args.bug}_{method}_{line}'
        mgr = get_manager(args.project, to_branch)
        src_dirs = mgr.src_dirs

        if not args.force and mgr.is_branch_exists(to_branch):
            logging.warn(f"Branch *{to_branch}* exists, please delete it before processing, \n> git branch -d {to_branch}\n> git branch -m {to_branch} bak-{to_branch}")
            continue

        logging.info(f"Checkout to from branch *{from_branch}*")
        mgr.checkout_branch(from_branch)

        cls_name = '/'.join(method.split('.')[:-1])
        for src_dir in src_dirs:
            file = src_dir / f'{cls_name.split("-")[0]}.java' if '-' in cls_name else src_dir / f'{cls_name}.java'
            if file.exists():
                break

        if not file.exists():
            logging.error(f'BUG: {str(file)} not exists')
            # import ipdb; ipdb.set_trace()
            continue

        with open(file, 'r') as fd:
            code = fd.read()

        logging.info(f"process file {str(file)}")
        pure_method = method.split('.')[-1]
        mutated_resp = mutate(code, pure_method, line, args.bug)
        mutated_code = mutated_resp['mutated_code']
        injected_bugs = mutated_resp['injected_bugs']
        if injected_bugs > 0:
            logging.info(f"Injected {injected_bugs} {args.bug} into code base");
            with open(file, 'w') as fp:
                fp.write(str(mutated_code))
            try:
                if not args.skip_compile:
                    logging.info("Compiling jmh jar ...")
                    mgr.compile(from_branch)
                mgr.checkout_new_branch(to_branch)
                mgr.commit_injected_bug(str(file.relative_to(mgr.cwd)), f'Injected bug {args.bug} at {pure_method}:{line}')
                logging.info(f"Inject bug {args.bug} into code successfully")
            except Exception as ex:
                logging.error(f"Fail to compile the code after injecting code {args.bug}, ex: {str(ex)}")
                # NOTE: revert the changed file
                # mgr.checkout_file(str(file))
            # NOTE: We just inject one bug into the codebase


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=True, help='rxjava, eclipse-collections, zipkin')
    parser.add_argument("--from_branch", type=str, default='jmh')
    parser.add_argument("--bug", type=str.upper, default='HWO', help='HWO,PTW,STS,EFL,SOC')
    # parser.add_argument('--common_methods_path', type=str, required=True)
    # parser.add_argument('--method', type=str, required=True)
    # parser.add_argument('--line', type=int, required=True)
    parser.add_argument("--parallel", action="store_true")
    parser.add_argument('--delay', type=int, default=1, help='use in HWO case, sleep for 1 ns by default')
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--skip_compile", action="store_true")
    args = parser.parse_args()
    main(args)
