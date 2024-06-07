import json
import os

# Get the output file
files = os.list_dir("_data")
# Read the output file
new_banner = json.load(open(f"_data/{files[0]}"))
print(new_banner)

# Update the existing file
json.dump(new_banner, open("banner.json", "w"))
