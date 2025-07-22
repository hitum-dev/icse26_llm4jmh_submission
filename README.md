# LLM4JMH: Studying the Use of LLMs for Generating Java Performance Microbenchmarks

This project is a replication package for the paper titled "LLM4JMH: Studying the Use of LLMs for Generating Java Performance Microbenchmarks".


# Folders Overview
- Data: Contains data files for each three studied subjects and benchmark suites, including results for each RQ.
- Scripts: Includes Python and Bash scripts for:
  - Generate JMH microbenchmarks from LLM (DeepSeek-V3).
  - Analyzing and generating reports on code coverage using JaCoCo.
  - Anaylyzing common methods benchmarked by all three benchmark suites.
  - Performance Mutant Tools
  - Analyzing the quality of JMH microbenchmarks, as indicators for domain specific selections
  - Analyzing Bug Size and RCIW
  - Script to replicate the Figures and Tables in the paper

# Prompt Template
## [Benchmark Generation] Analyze and Generate JMH Microbenchmark from Java Source Code
    Given a piece of Java source code. Please analyze it to determine if JMH benchmark tests are needed. If necessary, generate the corresponding JMH benchmark code in throughput benchmark mode for performance measurement, embedding relevant knowledge and best practices for performance testing in the generated code.

    Source Code:
    {src_code}

    Output instructions:
    + If it's not necessary to generate JMH code, output SKIP with reasons
    + If it's necessary to generate JMH code:
      - Do not add any explanation or commentary before or after the test code.
      - Wrap the entire code inside triple backticks like this:
      ```
      // your code here
      ```

## [Syntax/Compilation Repair] Fix Compilation Errors in LLM-Generated JMH Code
    Fix the bug in JMH code according to the compilation message

    JMH Code:
    {code}

    Comilation Message:
    {err_msg}

    Output instructions:
      - Do not add any explanation or commentary before or after the test code.
      - Wrap the entire code inside triple backticks like this:
      ```
      // your code here
      ```

## [Runtime Repair] Fix Runtime Exceptions in JMH Benchmark Code
    Fix the bug in JMH code according to the runtime exception

    JMH Code:
    {code}

    Runtime Message:
    {err_msg}

    Output instructions:
      - Do not add any explanation or commentary before or after the test code.
      - Wrap the entire code inside triple backticks like this:
      ```
      // your code here
      ```
