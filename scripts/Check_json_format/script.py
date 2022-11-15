import os
import sys
import json

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r") as file:
            json.load(file)
        print("Validate JSON!")
    else:
        print(f"{sys.argv[1]} not found")
else:
    print("Usage: checkjson.py <file>")