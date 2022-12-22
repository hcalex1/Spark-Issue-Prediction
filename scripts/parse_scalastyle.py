import pandas as pd

GIT_LOGS_PATH = "data/inputs/staticanalysis_output.txt"
OUTPUT_PATH   = "data/inputs/staticanalysis_output.csv"

output_content = pd.DataFrame()
with open(GIT_LOGS_PATH, "r") as file:

    for line in file:
        line_split = line.split()
        file = line_split[1].split("=/home/user1/prj/spark-3.0.0/")[1]
        (key, value) = line_split[2].split("=")[1].split(":")
        output_content.loc[file, key] = value

output_content[output_content.isna()] = 0

output_content["File"] = output_content.index
output_content.drop("MethodLength", axis=1, inplace=True)
output_content.to_csv(OUTPUT_PATH, index=False)