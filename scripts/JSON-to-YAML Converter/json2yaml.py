import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r") as source_file:
            source_content = json.load(source_file)
    else:
        print(f"ERROR: {sys.argv[1]} not found")
        exit(1)
else:
    print("Usage: json2yaml.py <source_file.json> [target_file.yaml]")

# Processing the conversion
output = yaml.dump(source_content)

# If no target file send to stdout
if len(sys.argv) < 3:
    print(output)
elif os.path.exists(sys.argv[2]):
    print(f"ERROR: {sys.argv[2]} already exists")
    exit(1)
else:
    with open(sys.argv[2], "w") as target_file:
        target_file.write(output)
