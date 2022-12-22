GIT_LOGS_PATH = "data/inputs/spark3.0_git_logs.txt"
OUTPUT_PATH   = "data/inputs/spark3.0_modified_files.csv"

output_content = "File,Commit hash,Commit timestamp,Subject\n"
with open(GIT_LOGS_PATH, "r") as log_file:

    for line in log_file:
        key   = line[0]
        value = line[2:-1]

        if key == 'H':
            hash = value
        elif key == 'T':
            timestamp = value
        elif key == 'S':
            subject = value.replace(',', ';')
        elif key == 'M':
            output_content += f"{value},{hash},{timestamp},{subject}\n"

with open(OUTPUT_PATH, "w") as output_file:
    output_file.write(output_content)