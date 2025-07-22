import platform
from typing import List, Union, Literal, Optional
import sys
import shutil
import subprocess
import os
from pathlib import Path
from collections import defaultdict, Counter
import re
import json
import logging


logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class Manager:
    def run_cmd(self, cmd: str, cwd: Optional[str] = None):
        _cwd = self.cwd if cwd is None else cwd
        try:
            result = subprocess.run(
                cmd,
                check=True,
                shell=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                cwd=_cwd,
            )
            return result
        except subprocess.CalledProcessError as cpe:
            logging.error(f"Command '{cmd}' failed with exit code {cpe.returncode}. Output: {cpe.output}")
            raise cpe
        except Exception as ex:
            logging.error(f'Command: {cmd}, unknown error: {str(ex)}')
            raise ex

    def check_java_version(self):
        cmd = "javac -version"
        result = self.run_cmd(cmd)
        if '17.' not in result.stdout:
            raise Exception(f"Invalid java version {result.stdout}, please run:\n> sudo apt install openjdk-17-jdk maven gradle -y\n> sudo update-alternatives --config java\n> sudo update-alternatives --config javac")

        cmd = "java -version"
        result = self.run_cmd(cmd)
        if platform.system() == 'Linux' and '21.' not in result.stdout:
            raise Exception(f"Invalid java version {result.stdout}, please run:\n> sudo apt install openjdk-21-jdk maven gradle -y\n> sudo update-alternatives --config java\n> sudo update-alternatives --config javac")

    def checkout_branch(self, branch: str):
        try:
            cmd = f'git checkout {branch}'
            self.run_cmd(cmd)
        except Exception as ex:
            cmd = f'git checkout -b {branch} origin/{branch}'
            self.run_cmd(cmd)

    def checkout_new_branch(self, branch: str):
        try:
            cmd = f'git checkout -b {branch}'
            self.run_cmd(cmd)
        except Exception as ex:
            cmd = f'git checkout {branch}'
            self.run_cmd(cmd)

    def checkout_file(self, file: str):
        cmd = f'git checkout {file}'
        self.run_cmd(cmd)

    def is_branch_exists(self, branch: str) -> bool:
        cmd = f"git show-ref --verify refs/heads/{branch}"
        try:
            result = self.run_cmd(cmd)
            return result.returncode == 0
        except Exception as ex:
            return False

    def commit_injected_bug(self, file: str, msg: str):
        cmd = f'git add {file}'
        self.run_cmd(cmd)
        cmd = f'git commit -m "{msg}"'
        self.run_cmd(cmd)

    def list_benchmark_methods(self, jar_path: Path) -> List[str]:
        cmd = f'java  --add-opens java.base/java.io=ALL-UNNAMED -jar {jar_path.resolve()} -l | grep "{self.package}"'
        methods = self.run_cmd(cmd)
        methods = methods.stdout.split('\n')
        return sorted([x for x in methods if x])

    def get_all_subpackages(self) -> List[str]:
        packages = set()
        pattern = r'^\s*package\s+([a-zA-Z0-9_.]+)\s*;'
        for src_dir in self.src_dirs:
            files = sorted([x for x in src_dir.rglob('*.java')])
            for file in files:
                if file.name == 'package-info.java':
                    continue
                with open(file, 'r') as fd:
                    java_source = fd.read()
                found = re.search(pattern, java_source, re.MULTILINE)
                if found:
                    package_name = found.group(1)
                    packages.add(package_name)
        return sorted(list(packages))

    def unzip_jar_for_class_dirs(self):
        import zipfile
        import shutil
        target_dir = Path(f"./tmp/{self.cwd}/{self.branch}")
        # if target_dir.exists():
        #     shutil.rmtree(target_dir.resolve())
        target_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(self.jar_path, 'r') as jar:
            # jar.extractall(target_dir.resolve())
            for member in jar.infolist():
                if member.is_dir():
                    continue
                if self.package.replace('.', '/') in member.filename:
                    file_path = target_dir / member.filename
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    with jar.open(member) as source, open(file_path, "wb") as target:
                        target.write(source.read())
        self.class_dirs = [Path(f'{(target_dir / self.package.replace(".", "/")).resolve()}')]
        return self.class_dirs

    def compile_if_needed(self, branch: str):
        jar_path = Path(f'./tmp/{self.cwd}/{branch}') / self.jar_path.name
        if not jar_path.exists():
            jar_path.parent.mkdir(parents=True, exist_ok=True)
            logging.info(f"Checkout to branch [{self.cwd}]-[{branch}]")
            self.checkout_branch(branch)
            logging.info(f"Compiling jmh jar for [{self.cwd}]...")
            self.compile(branch)
            logging.info("Compiled jmh jar for [{self.cwd}] successfully")
            shutil.copy(self.jar_path, jar_path)


class RxJavaManager(Manager):
    cwd = 'projects/rxjava'
    package = 'io.reactivex.rxjava3'

    def __init__(self, branch: str):
        self.check_java_version()
        cwd = self.cwd
        self.branch = branch
        self.src_dirs = [Path(f'{cwd}/src/main/java')]
        self.test_dirs = [Path(f'{cwd}/src/test/java')]

        self.class_dirs = [Path(f'{cwd}/build/classes/java/main')]
        self.jar_path = Path(f'{cwd}/build/libs/rxjava-3.0.0-SNAPSHOT-jmh.jar')
        if 'llm2jmh-junit' in branch:
            self.jmh_dir = Path(f'{cwd}/llm2jmh-junit/java')
        elif 'llm2jmh' in branch:
            self.jmh_dir = Path(f'{cwd}/llm2jmh/java')
        elif 'ju2jmh' in branch:
            self.jmh_dir = Path(f'{cwd}/ju2jmh/java')
        else:
            self.jmh_dir = Path(f'{cwd}/src/jmh/java')
        # self.llm2jmh_dir = Path(f'{cwd}/llm2jmh/java')
        # self.ju2jmh_dir = Path(f'{cwd}/ju2jmh/java')
        self.save_coverage_dir = Path(f'results/{cwd}/coverage/{branch}')
        self.save_benchmark_dir =Path(f'results/{cwd}/benchmark/{branch}')
        self.save_coverage_dir.mkdir(parents=True, exist_ok=True)
        self.save_benchmark_dir.mkdir(parents=True, exist_ok=True)
        self.save_coverage_html_dir = Path(f'results/{cwd}/coverage_html/{branch}')
        self.save_coverage_html_dir.mkdir(parents=True, exist_ok=True)

    def compile(self, path: Optional[str] = None):
        if self.jar_path.exists():
            self.jar_path.unlink()
        cmd = './gradlew clean jmhJar'
        self.run_cmd(cmd)


class EclipseCollectionManager(Manager):
    cwd = 'projects/eclipse-collections'
    package = 'org.eclipse.collections'

    def __init__(self, branch: str):
        self.check_java_version()
        cwd = self.cwd
        self.branch = branch
        self.src_dirs = sorted([
            Path(f'{cwd}/eclipse-collections/src/main/java'),
            Path(f'{cwd}/eclipse-collections-api/src/main/java'),
            Path(f'{cwd}/eclipse-collections-forkjoin/src/main/java'),
        ])
        self.test_dirs = sorted([
            Path(f'{cwd}/unit-tests/src/test/java'),
        ])
        self.class_dirs = sorted([
            Path(f'{cwd}/eclipse-collections/target/classes'),
            Path(f'{cwd}/eclipse-collections-api/target/classes'),
            Path(f'{cwd}/eclipse-collections-forkjoin/target/classes'),
            Path(f'{cwd}/{branch}/target/classes')
        ])
        if 'llm2jmh-junit' in branch:
            self.jmh_dir = Path(f'{cwd}/llm2jmh-junit/src/main/java')
            self.jar_path = Path(f'{cwd}/llm2jmh-junit/target/microbenchmarks.jar')
        elif 'llm2jmh' in branch:
            self.jmh_dir = Path(f'{cwd}/llm2jmh/src/main/java')
            self.jar_path = Path(f'{cwd}/llm2jmh/target/microbenchmarks.jar')
        elif 'ju2jmh' in branch:
            self.jmh_dir = Path(f'{cwd}/ju2jmh/src/main/java')
            self.jar_path = Path(f'{cwd}/ju2jmh/target/microbenchmarks.jar')
        else:
            self.jmh_dir = Path(f'{cwd}/jmh-tests/src/main/java')
            self.jar_path = Path(f'{cwd}/jmh-tests/target/microbenchmarks.jar')

        self.save_coverage_dir = Path(f'results/{cwd}/coverage/{branch}')
        self.save_benchmark_dir =Path(f'results/{cwd}/benchmark/{branch}')
        self.save_coverage_dir.mkdir(parents=True, exist_ok=True)
        self.save_benchmark_dir.mkdir(parents=True, exist_ok=True)
        self.save_coverage_html_dir = Path(f'results/{cwd}/coverage_html/{branch}')
        self.save_coverage_html_dir.mkdir(parents=True, exist_ok=True)

    def compile(self, path: Optional[str]):
        if self.jar_path.exists():
            self.jar_path.unlink()
        # cmd = 'mvn install -DskipTests=true'
        # self.run_cmd(cmd)
        if 'llm2jmh-junit' in path:
            path = 'llm2jmh-junit'
        elif 'llm2jmh' in path:
            path = 'llm2jmh'
        elif 'ju2jmh' in path:
            path = 'ju2jmh'
        else:
            path = 'jmh-tests'

        cmd = "mvn clean package -DskipTests=true"
        cwd = f'{self.cwd}/{path}'
        self.run_cmd(cmd, cwd)


class ZipkinManager(Manager):
    cwd = 'projects/zipkin'
    package = 'zipkin2'

    def __init__(self, branch: str):
        # self.check_java_version()
        cwd = self.cwd
        self.branch = branch
        self.src_dirs = sorted([
            Path(f'{cwd}/zipkin/src/main/java'),
            Path(f'{cwd}/zipkin-collector/core/src/main/java'),
            # Path(f'{cwd}/zipkin-collector/activemq/src/main/java'),
            # Path(f'{cwd}/zipkin-collector/kafka/src/main/java'),
            # Path(f'{cwd}/zipkin-collector/pulsar/src/main/java'),
            # Path(f'{cwd}/zipkin-collector/rabbitmq/src/main/java'),
            # Path(f'{cwd}/zipkin-collector/scribe/src/main/java'),
            Path(f'{cwd}/zipkin-server/src/main/java'),
            Path(f'{cwd}/benchmarks/src/main/java'),
            Path(f'{cwd}/zipkin-tests/src/main/java'),
            # Path(f'{cwd}/zipkin-storage/cassandra/src/main/java'),
            # Path(f'{cwd}/zipkin-storage/elasticsearch/src/main/java'),
            # Path(f'{cwd}/zipkin-storage/mysql-v1/src/main/java'),
            # Path(f'{cwd}/{branch}/src/main/java'),
        ])
        self.test_dirs = sorted([
            Path(f'{cwd}/zipkin-junit/src/test/java'),
            Path(f'{cwd}/zipkin-tests/src/test/java'),
            Path(f'{cwd}/zipkin-collector/core/src/test/java'),
            Path(f'{cwd}/zipkin-server/core/src/test/java'),
        ])
        self.class_dirs = sorted([
            # Path(f'{cwd}/zipkin/target/classes'),
            # Path(f'{cwd}/zipkin-collector/core/target/classes'),
            # Path(f'{cwd}/zipkin-collector/activemq/target/classes'),
            # Path(f'{cwd}/zipkin-collector/kafka/target/classes'),
            # Path(f'{cwd}/zipkin-collector/pulsar/target/classes'),
            # Path(f'{cwd}/zipkin-collector/rabbitmq/target/classes'),
            # Path(f'{cwd}/zipkin-collector/scribe/target/classes'),
            # Path(f'{cwd}/zipkin-server/target/classes'),
            # Path(f'{cwd}/zipkin-storage/cassandra/target/classes'),
            # Path(f'{cwd}/zipkin-storage/elasticsearch/target/classes'),
            # Path(f'{cwd}/zipkin-storage/mysql-v1/target/classes'),
            # Path(f'{cwd}/{branch}/target/classes'),
            # Path(f'./tmp/zipkin_classes')
        ])
        # self.jar_path = Path(f'{cwd}/{branch}/target/benchmarks.jar')
        if 'llm2jmh-junit' in branch:
            self.jmh_dir = Path(f'{cwd}/llm2jmh-junit/src/main/java')
            self.jar_path = Path(f'{cwd}/llm2jmh-junit/target/benchmarks.jar')
        elif 'llm2jmh' in branch:
            self.jmh_dir = Path(f'{cwd}/llm2jmh/src/main/java')
            self.jar_path = Path(f'{cwd}/llm2jmh/target/benchmarks.jar')
        elif 'ju2jmh' in branch:
            self.jmh_dir = Path(f'{cwd}/ju2jmh/src/main/java')
            self.jar_path = Path(f'{cwd}/ju2jmh/target/benchmarks.jar')
        else:
            self.jmh_dir = Path(f'{cwd}/benchmarks/src/main/java')
            self.jar_path = Path(f'{cwd}/benchmarks/target/benchmarks.jar')
        # self.class_dirs = [self.jar_path]
        self.save_coverage_dir = Path(f'results/{cwd}/coverage/{branch}')
        self.save_benchmark_dir = Path(f'results/{cwd}/benchmark/{branch}')
        self.save_coverage_dir.mkdir(parents=True, exist_ok=True)
        self.save_benchmark_dir.mkdir(parents=True, exist_ok=True)
        self.save_coverage_html_dir = Path(f'results/{cwd}/coverage_html/{branch}')
        self.save_coverage_html_dir.mkdir(parents=True, exist_ok=True)

    def get_all_subpackages(self) -> List[str]:
        all_subpackages = super().get_all_subpackages()
        subpackages = []
        for pkg in all_subpackages:
            if pkg != 'zipkin2':
                subpackages.append(pkg)
        return subpackages

    def check_java_version(self):
        cmd = "javac -version"
        result = self.run_cmd(cmd)
        if '11.' not in result.stdout:
            raise Exception(f"Invalid java version {result.stdout}, please run:\n> sudo apt install openjdk-11-jdk maven gradle -y\n> sudo update-alternatives --config java\n> sudo update-alternatives --config javac")

        cmd = "java -version"
        result = self.run_cmd(cmd)
        if '21.' not in result.stdout:
            raise Exception(f"Invalid java version {result.stdout}, please run:\n> sudo apt install openjdk-21-jdk maven gradle -y\n> sudo update-alternatives --config java\n> sudo update-alternatives --config javac")

    def compile(self, path: Optional[str]):
        if self.jar_path.exists():
            self.jar_path.unlink()
        # cmd = 'mvn install -DskipTests=true -Denforcer.skip=true'
        # self.run_cmd(cmd)
        if 'llm2jmh-junit' in path:
            path = 'llm2jmh-junit'
        elif 'llm2jmh' in path:
            path = 'llm2jmh'
        elif 'ju2jmh' in path:
            path = 'ju2jmh'
        else:
            path = 'benchmarks'

        cmd = "mvn clean package -DskipTests=true -Danimal.sniffer.skip=true -Denforcer.skip=true"
        cwd = f'{self.cwd}/{path}'
        self.run_cmd(cmd, cwd)


class Flink17799Manager(Manager):
    cwd = 'projects/flink-17799'
    package = 'org.apache.flink'

    def __init__(self, branch: str):
        # self.check_java_version()
        cwd = self.cwd
        self.branch = branch
        self.src_dirs = sorted([
            # Path(f'{cwd}/flink-annotations/src/main/java'),
            # Path(f'{cwd}/flink-core/src/main/java'),
            # Path(f'{cwd}/flink-java/src/main/java'),
            # Path(f'{cwd}/flink-clients/src/main/java'),
            Path(f'{cwd}/flink-runtime/src/main/java'),
            # Path(f'{cwd}/flink-streaming-java/src/main/java'),
            # Path(f'{cwd}/flink-queryable-state/flink-queryable-state-runtime/src/main/java'),
            # Path(f'{cwd}/flink-queryable-state/flink-queryable-state-client-java/src/main/java'),
            # Path(f'{cwd}/flink-state-backends/flink-statebackend-heap-spillable/src/main/java'),
            # Path(f'{cwd}/flink-state-backends/flink-statebackend-rocksdb/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-sql-client/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-sql-parser/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-sql-parser-hive/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-table-api-java/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-table-common/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-table-planner/src/main/java'),
            # Path(f'{cwd}/flink-optimizer/src/main/java'),
            # Path(f'{cwd}/flink-libraries/flink-cep/src/main/java'),
            # Path(f'{cwd}/flink-formats/flink-csv/src/main/java'),
            # Path(f'{cwd}/flink-formats/flink-json/src/main/java'),
            # Path(f'{cwd}/flink-formats/flink-avro/src/main/java'),
            # Path(f'{cwd}/flink-formats/flink-parquet/src/main/java'),
        ])
        self.test_dirs = sorted([
            Path(f'{cwd}/flink-annotations/src/test/java'),
            Path(f'{cwd}/flink-core/src/test/java'),
            Path(f'{cwd}/flink-java/src/test/java'),
            Path(f'{cwd}/flink-clients/src/test/java'),
            Path(f'{cwd}/flink-runtime/src/test/java'),
            Path(f'{cwd}/flink-streaming-java/src/test/java'),
            Path(f'{cwd}/flink-queryable-state/flink-queryable-state-runtime/src/test/java'),
            Path(f'{cwd}/flink-queryable-state/flink-queryable-state-client-java/src/test/java'),
            Path(f'{cwd}/flink-state-backends/flink-statebackend-heap-spillable/src/test/java'),
            Path(f'{cwd}/flink-state-backends/flink-statebackend-rocksdb/src/test/java'),
            Path(f'{cwd}/flink-table/flink-sql-client/src/test/java'),
            Path(f'{cwd}/flink-table/flink-sql-parser/src/test/java'),
            Path(f'{cwd}/flink-table/flink-sql-parser-hive/src/test/java'),
            Path(f'{cwd}/flink-table/flink-table-api-java/src/test/java'),
            Path(f'{cwd}/flink-table/flink-table-common/src/test/java'),
            Path(f'{cwd}/flink-table/flink-table-planner/src/test/java'),
            Path(f'{cwd}/flink-optimizer/src/test/java'),
            Path(f'{cwd}/flink-libraries/flink-cep/src/test/java'),
            Path(f'{cwd}/flink-formats/flink-csv/src/test/java'),
            Path(f'{cwd}/flink-formats/flink-json/src/test/java'),
            Path(f'{cwd}/flink-formats/flink-avro/src/test/java'),
            Path(f'{cwd}/flink-formats/flink-parquet/src/test/java'),
            Path(f'{cwd}/flink-tests/src/test/java'),
        ])
        self.class_dirs = sorted([

        ])
        # self.jar_path = Path(f'{cwd}/{branch}/target/benchmarks.jar')
        if 'llm2jmh-junit' in branch:
            self.jmh_dir = Path(f'{cwd}/llm2jmh-junit/src/main/java')
            self.jar_path = Path(f'{cwd}/llm2jmh-junit/target/benchmarks.jar')
        elif 'llm2jmh' in branch:
            self.jmh_dir = Path(f'{cwd}/llm2jmh/src/main/java')
            self.jar_path = Path(f'{cwd}/llm2jmh/target/benchmarks.jar')
        elif 'ju2jmh' in branch:
            self.jmh_dir = Path(f'{cwd}/ju2jmh/src/main/java')
            self.jar_path = Path(f'{cwd}/ju2jmh/target/benchmarks.jar')
        else:
            self.jmh_dir = Path(f'{cwd}/benchmarks/src/main/java')
            self.jar_path = Path(f'{cwd}/benchmarks/target/benchmarks.jar')
        # self.class_dirs = [self.jar_path]
        self.save_coverage_dir = Path(f'results/{cwd}/coverage/{branch}')
        self.save_benchmark_dir = Path(f'results/{cwd}/benchmark/{branch}')
        self.save_coverage_dir.mkdir(parents=True, exist_ok=True)
        self.save_benchmark_dir.mkdir(parents=True, exist_ok=True)
        self.save_coverage_html_dir = Path(f'results/{cwd}/coverage_html/{branch}')
        self.save_coverage_html_dir.mkdir(parents=True, exist_ok=True)

    def get_all_subpackages(self) -> List[str]:
        all_subpackages = super().get_all_subpackages()
        subpackages = []
        for pkg in all_subpackages:
            if pkg != 'org.apache.flink':
                subpackages.append(pkg)
        return subpackages

    def check_java_version(self):
        cmd = "javac -version"
        result = self.run_cmd(cmd)
        if '8.' not in result.stdout:
            raise Exception(f"Invalid java version {result.stdout}, please run:\n> sudo apt install openjdk-11-jdk maven gradle -y\n> sudo update-alternatives --config java\n> sudo update-alternatives --config javac")

        cmd = "java -version"
        result = self.run_cmd(cmd)
        if '21.' not in result.stdout:
            raise Exception(f"Invalid java version {result.stdout}, please run:\n> sudo apt install openjdk-21-jdk maven gradle -y\n> sudo update-alternatives --config java\n> sudo update-alternatives --config javac")

    def compile(self, path: Optional[str]):
        if self.jar_path.exists():
            self.jar_path.unlink()
        # cmd = 'mvn install -DskipTests=true -Denforcer.skip=true -Drat.skip=true '
        # self.run_cmd(cmd)
        if 'llm2jmh-junit' in path:
            path = 'llm2jmh-junit'
        elif 'llm2jmh' in path:
            path = 'llm2jmh'
        elif 'ju2jmh' in path:
            path = 'ju2jmh'
        else:
            path = 'flink-benchmarks'

        cmd = "mvn clean package -DskipTests=true -Danimal.sniffer.skip=true -Denforcer.skip=true -Dcheckstyle.skip -Drat.skip=true"
        cwd = f'{self.cwd}/{path}'
        self.run_cmd(cmd, cwd)


class Flink16536Manager(Manager):
    cwd = 'projects/flink-16536'
    package = 'org.apache.flink'

    def __init__(self, branch: str):
        # self.check_java_version()
        cwd = self.cwd
        self.branch = branch
        self.src_dirs = sorted([
            # Path(f'{cwd}/flink-annotations/src/main/java'),
            # Path(f'{cwd}/flink-core/src/main/java'),
            # Path(f'{cwd}/flink-java/src/main/java'),
            # Path(f'{cwd}/flink-clients/src/main/java'),
            Path(f'{cwd}/flink-runtime/src/main/java'),
            # Path(f'{cwd}/flink-streaming-java/src/main/java'),
            # Path(f'{cwd}/flink-queryable-state/flink-queryable-state-runtime/src/main/java'),
            # Path(f'{cwd}/flink-queryable-state/flink-queryable-state-client-java/src/main/java'),
            # Path(f'{cwd}/flink-state-backends/flink-statebackend-heap-spillable/src/main/java'),
            # Path(f'{cwd}/flink-state-backends/flink-statebackend-rocksdb/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-sql-client/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-sql-parser/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-sql-parser-hive/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-table-api-java/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-table-common/src/main/java'),
            # Path(f'{cwd}/flink-table/flink-table-planner/src/main/java'),
            # Path(f'{cwd}/flink-optimizer/src/main/java'),
            # Path(f'{cwd}/flink-libraries/flink-cep/src/main/java'),
            # Path(f'{cwd}/flink-formats/flink-csv/src/main/java'),
            # Path(f'{cwd}/flink-formats/flink-json/src/main/java'),
            # Path(f'{cwd}/flink-formats/flink-avro/src/main/java'),
            # Path(f'{cwd}/flink-formats/flink-parquet/src/main/java'),
        ])
        self.test_dirs = sorted([
            Path(f'{cwd}/flink-annotations/src/test/java'),
            Path(f'{cwd}/flink-core/src/test/java'),
            Path(f'{cwd}/flink-java/src/test/java'),
            Path(f'{cwd}/flink-clients/src/test/java'),
            Path(f'{cwd}/flink-runtime/src/test/java'),
            Path(f'{cwd}/flink-streaming-java/src/test/java'),
            Path(f'{cwd}/flink-queryable-state/flink-queryable-state-runtime/src/test/java'),
            Path(f'{cwd}/flink-queryable-state/flink-queryable-state-client-java/src/test/java'),
            Path(f'{cwd}/flink-state-backends/flink-statebackend-heap-spillable/src/test/java'),
            Path(f'{cwd}/flink-state-backends/flink-statebackend-rocksdb/src/test/java'),
            Path(f'{cwd}/flink-table/flink-sql-client/src/test/java'),
            Path(f'{cwd}/flink-table/flink-sql-parser/src/test/java'),
            Path(f'{cwd}/flink-table/flink-sql-parser-hive/src/test/java'),
            Path(f'{cwd}/flink-table/flink-table-api-java/src/test/java'),
            Path(f'{cwd}/flink-table/flink-table-common/src/test/java'),
            Path(f'{cwd}/flink-table/flink-table-planner/src/test/java'),
            Path(f'{cwd}/flink-optimizer/src/test/java'),
            Path(f'{cwd}/flink-libraries/flink-cep/src/test/java'),
            Path(f'{cwd}/flink-formats/flink-csv/src/test/java'),
            Path(f'{cwd}/flink-formats/flink-json/src/test/java'),
            Path(f'{cwd}/flink-formats/flink-avro/src/test/java'),
            Path(f'{cwd}/flink-formats/flink-parquet/src/test/java'),
            Path(f'{cwd}/flink-tests/src/test/java'),
        ])
        self.class_dirs = sorted([

        ])
        # self.jar_path = Path(f'{cwd}/{branch}/target/benchmarks.jar')
        if 'llm2jmh-junit' in branch:
            self.jmh_dir = Path(f'{cwd}/llm2jmh-junit/src/main/java')
            self.jar_path = Path(f'{cwd}/llm2jmh-junit/target/benchmarks.jar')
        elif 'llm2jmh' in branch:
            self.jmh_dir = Path(f'{cwd}/llm2jmh/src/main/java')
            self.jar_path = Path(f'{cwd}/llm2jmh/target/benchmarks.jar')
        elif 'ju2jmh' in branch:
            self.jmh_dir = Path(f'{cwd}/ju2jmh/src/main/java')
            self.jar_path = Path(f'{cwd}/ju2jmh/target/benchmarks.jar')
        else:
            self.jmh_dir = Path(f'{cwd}/benchmarks/src/main/java')
            self.jar_path = Path(f'{cwd}/benchmarks/target/benchmarks.jar')
        # self.class_dirs = [self.jar_path]
        self.save_coverage_dir = Path(f'results/{cwd}/coverage/{branch}')
        self.save_benchmark_dir = Path(f'results/{cwd}/benchmark/{branch}')
        self.save_coverage_dir.mkdir(parents=True, exist_ok=True)
        self.save_benchmark_dir.mkdir(parents=True, exist_ok=True)
        self.save_coverage_html_dir = Path(f'results/{cwd}/coverage_html/{branch}')
        self.save_coverage_html_dir.mkdir(parents=True, exist_ok=True)

    def get_all_subpackages(self) -> List[str]:
        all_subpackages = super().get_all_subpackages()
        subpackages = []
        for pkg in all_subpackages:
            if pkg != 'org.apache.flink':
                subpackages.append(pkg)
        return subpackages

    def check_java_version(self):
        cmd = "javac -version"
        result = self.run_cmd(cmd)
        if '8.' not in result.stdout:
            raise Exception(f"Invalid java version {result.stdout}, please run:\n> sudo apt install openjdk-11-jdk maven gradle -y\n> sudo update-alternatives --config java\n> sudo update-alternatives --config javac")

        cmd = "java -version"
        result = self.run_cmd(cmd)
        if '21.' not in result.stdout:
            raise Exception(f"Invalid java version {result.stdout}, please run:\n> sudo apt install openjdk-21-jdk maven gradle -y\n> sudo update-alternatives --config java\n> sudo update-alternatives --config javac")

    def compile(self, path: Optional[str]):
        if self.jar_path.exists():
            self.jar_path.unlink()
        # cmd = 'mvn install -DskipTests=true -Denforcer.skip=true -Drat.skip=true '
        # self.run_cmd(cmd)
        if 'llm2jmh-junit' in path:
            path = 'llm2jmh-junit'
        elif 'llm2jmh' in path:
            path = 'llm2jmh'
        elif 'ju2jmh' in path:
            path = 'ju2jmh'
        else:
            path = 'flink-benchmarks'

        cmd = "mvn clean package -DskipTests=true -Danimal.sniffer.skip=true -Denforcer.skip=true -Dcheckstyle.skip -Drat.skip=true"
        cwd = f'{self.cwd}/{path}'
        self.run_cmd(cmd, cwd)

def get_manager(project: str, branch: str) -> Manager:
    if project == 'rxjava':
        mgr = RxJavaManager(branch)
    elif project == 'eclipse-collections':
        mgr = EclipseCollectionManager(branch)
    elif project == 'zipkin':
        mgr = ZipkinManager(branch)
    elif project == 'flink-17799':
        mgr = Flink17799Manager(branch)
    elif project == 'flink-16536':
        mgr = Flink16536Manager(branch)
    else:
        raise Exception(f'Unknown project {project}')
    return mgr
