# Spark Issue Prediction

## Inputs
- [Jira bugs](https://issues.apache.org/jira/browse/SPARK-39079?jql=project%20%3D%20SPARK%20AND%20issuetype%20%3D%20Bug%20AND%20status%20in%20(Resolved%2C%20Closed)%20AND%20affectedVersion%20%3D%203.0.0%20ORDER%20BY%20updated%20DESC) affecting Apache Spark version 3.0.0
- Apache Spark version 3.0.0 [source code](https://github.com/apache/spark/releases/tag/v3.0.0)
- Apache Spark branch-3.0 [commits](https://github.com/apache/spark/commits/branch-3.0)

## Data extraction
Jira bugs were downloaded as csv to `data/inputs/spark_bugs_3.0.0.csv`.

Commit history from the Apache project branch-3.0 branch were saved to `data/inputs/spark3.0_git_logs.txt` using the following command:
 ``` bash
 git log --name-status --pretty=format:"H %H%nT %ct%nS %s"
 ```
 They are then parsed using the script in `scripts/parse_git_logs.py` and saved to `data/inputs/spark3.0_modified_files.csv`