## Query

    project = FLINK AND (summary ~ "performance" OR description ~ "performance" OR labels in ("performance", "perf", "slow", "slowdown"))

### SUCC FLINK-14346
    + [[https://issues.apache.org/jira/browse/FLINK-14346][FLINK-14346]] introduced this issue
      #+begin_src shell
        gh pr checkout 10358
      #+end_src
    + [[https://issues.apache.org/jira/browse/FLINK-15171][FLINK-15171]] fixed this issue

    + bug size 1%, cases: 54

### SUCC [[https://issues.apache.org/jira/browse/FLINK-16536][FLINK-16536]] (Y)
    + FLINK-16536 introduced this issue
      #+begin_src shell
        gh pr checkout 11687
      #+end_src
    + FLINK-17799 fixed this issue

    +   bug size 1%, 5%, 10%, cases: 12
### SUCC [[https://issues.apache.org/jira/browse/FLINK-17547][FLINK-17547]] (Y)
    + FLINK-17547 introduced this issue
      #+begin_src shell
        gh pr checkout 12120
      #+end_src
    + FLINK-17842 fixed this issue
    + bug size 1%, 5%, 10%, 50%, 90%, cases: 42

### SUCC [[https://issues.apache.org/jira/browse/FLINK-26279][FLINK-26279]] (Y)
    + FLINK-26279 introduced this issue
      #+begin_src shell
        gh pr checkout 18991
      #+end_src
    + [[https://issues.apache.org/jira/browse/FLINK-26864][FLINK-26864]] fixed this issue
    + bug size: 1%, 5%, cases: 14

### SUCC [[https://issues.apache.org/jira/browse/FLINK-31656][FLINK-31656]] (Y)
    + FLINK-31656 introduced this issue
      #+begin_src shell
        gh pr checkout 22298 # or
        gh pr checkout 22325
      #+end_src
    + [[https://issues.apache.org/jira/browse/FLINK-31745][FLINK-31745]] fixed this issue
    + bug size: 1%, cases: 25
### SUCC [[https://issues.apache.org/jira/browse/FLINK-34954][FLINK-34954]] (Y)
    + FLINK-34954 introduced this issue
      #+begin_src shell
        gh pr checkout 24586
      #+end_src
    + [[https://issues.apache.org/jira/browse/FLINK-35215][FLINK-35215]]
    + bug size: 1%, cases:  6

### FAIL [[https://issues.apache.org/jira/browse/FLINK-14304][FLINK-14304]]
    + [[https://issues.apache.org/jira/browse/FLINK-14304][FLINK-14304]] introduced this issue
      #+begin_src shell
        gh pr checkout 10009
      #+end_src
    + [[https://issues.apache.org/jira/browse/FLINK-14747][FLINK-14747]] fixed this issue
    + cases: 3
### FAIL [[https://issues.apache.org/jira/browse/FLINK-19010][FLINK-19010]] (N)
    + FLINK-19010 introduced this bug
      #+begin_src shell
        gh pr checkout 22772
      #+end_src
    + [[https://issues.apache.org/jira/browse/FLINK-32685][FLINK-32685]] fixed this issue
    + case: 4
### FAIL [[https://issues.apache.org/jira/browse/FLINK-23452][FLINK-23452]] (N)
    + FLINK-23452 introduced this issue
    #+begin_src shell
      gh pr checkout 16556
    #+end_src
    + [[https://issues.apache.org/jira/browse/FLINK-23560][FLINK-23560]] fixed this issue
    + cases: 2
### FAIL [[https://issues.apache.org/jira/browse/FLINK-25511][FLINK-25511]] (N)
    + FLINK-25511 introduced this issue
      #+begin_src shell
        gh pr checkout 19550
      #+end_src
    + [[https://issues.apache.org/jira/browse/FLINK-27556][FLINK-27556]] fixed this issue
    + cases: 6
### FAIL [[https://issues.apache.org/jira/browse/FLINK-30533][FLINK-30533]] (N)
    + [[https://issues.apache.org/jira/browse/FLINK-30533][FLINK-30533]] introduced this issue
      #+begin_src shell
        gh pr checkout 21576
      #+end_src
    + [[https://issues.apache.org/jira/browse/FLINK-30623][FLINK-30623]] fixed this issue
    + cases: 3
