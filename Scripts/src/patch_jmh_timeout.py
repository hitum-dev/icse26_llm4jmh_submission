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


# # Constants
# TIMEOUT_TIME = 1500
# TIMEOUT_UNIT = "TimeUnit.MILLISECONDS"

# def add_timeout_if_needed(method: MethodDeclaration):
#     # Check if already has @Timeout
#     for annotation in method.getAnnotations():
#         if annotation.getNameAsString() == "Timeout":
#             return  # Already has timeout

#     # Create new @Timeout annotation
#     pairs = NodeList()
#     pairs.add(MemberValuePair("time", StaticJavaParser.parseExpression(str(TIMEOUT_TIME))))
#     pairs.add(MemberValuePair("timeUnit", StaticJavaParser.parseExpression(TIMEOUT_UNIT)))

#     timeout_annotation = NormalAnnotationExpr(Name("Timeout"), pairs)
#     method.addAnnotation(timeout_annotation)

# def ensure_imports(compilation_unit):
#     existing_imports = {imp.getNameAsString() for imp in compilation_unit.getImports()}
#     needed_imports = {
#         "org.openjdk.jmh.annotations.Timeout",
#         "java.util.concurrent.TimeUnit"
#     }
#     for imp in needed_imports - existing_imports:
#         compilation_unit.addImport(imp)


# def patch_file(file_path: Path):
#     from com.github.javaparser import StaticJavaParser
#     from com.github.javaparser.ast.expr import NormalAnnotationExpr, Name, MemberValuePair, FieldAccessExpr
#     from com.github.javaparser.ast.expr import NameExpr
#     from com.github.javaparser.ast.body import MethodDeclaration
#     from com.github.javaparser.ast.Modifier import Keyword
#     from com.github.javaparser.ast.body import ClassOrInterfaceDeclaration
#     from com.github.javaparser.ast import ImportDeclaration

#     with file_path.open('r', encoding='utf-8') as f:
#         content = f.read()

#     cu = StaticJavaParser.parse(content)
#     for type_decl in cu.getTypes():
#         if isinstance(type_decl, ClassOrInterfaceDeclaration):
#             process_methods(type_decl)

#     # Ensure required imports
#     ensure_imports(cu)


def patch_file(file_path: Path):
    from com.github.javaparser import StaticJavaParser
    from com.github.javaparser.ast.expr import NormalAnnotationExpr, Name, MemberValuePair, FieldAccessExpr
    from com.github.javaparser.ast.expr import NameExpr
    from com.github.javaparser.ast.body import MethodDeclaration
    from com.github.javaparser.ast.Modifier import Keyword
    from com.github.javaparser.ast.body import ClassOrInterfaceDeclaration
    from com.github.javaparser.ast import ImportDeclaration

    with file_path.open('r', encoding='utf-8') as f:
        content = f.read()

    cu = StaticJavaParser.parse(content)

    # Ensure required imports exist
    imports = [imp.getNameAsString() for imp in cu.getImports()]
    if 'org.openjdk.jmh.annotations.Timeout' not in imports:
        cu.addImport('org.openjdk.jmh.annotations.Timeout')
    if 'java.util.concurrent.TimeUnit' not in imports:
        cu.addImport('java.util.concurrent.TimeUnit')

    def process_methods(cls: ClassOrInterfaceDeclaration):
        for method in cls.getMethods():
            # for annotation in method.getAnnotations():
            #     if annotation.getNameAsString().endsWith("Benchmark"):
            if method.isAnnotationPresent("Benchmark") and not method.isAnnotationPresent("Timeout"):
                    # Create and add @Timeout annotation
                    timeout_annotation = NormalAnnotationExpr()
                    timeout_annotation.setName(Name("Timeout"))
                    timeout_annotation.addPair("time", "2")
                    timeout_annotation.addPair("timeUnit", FieldAccessExpr(NameExpr("TimeUnit"), "SECONDS"))
                    method.addAnnotation(timeout_annotation)

        # Process inner classes

        for member in cls.getMembers():
            if isinstance(member, ClassOrInterfaceDeclaration):
                process_methods(member)

    for type_decl in cu.getTypes():
        if isinstance(type_decl, ClassOrInterfaceDeclaration):
            process_methods(type_decl)

    with file_path.open('w', encoding='utf-8') as f:
        f.write(str(cu))
        print(f"✅ Patched: {file_path}")


@patch_jpype
def main(args):
    branches = args.branch
    for branch in branches:
        mgr = get_manager(args.project, branch)
        mgr.checkout_branch(branch)
        for path in Path(mgr.jmh_dir).rglob("*.java"):
            # if 'ju2jmh/java/io/reactivex/rxjava3/parallel/ParallelPeekTest.java' not in str(path):
            #     continue
            patch_file(path)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, required=True, help='rxjava, eclipse-collections')
    parser.add_argument("--branch", action="append")
    args = parser.parse_args()
    main(args)
