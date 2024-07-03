import json
import os

# Get the output file
if not os.path.exists("_data"):
    os.makedirs("_data")

files = os.listdir("_data")
print(files)
# Read the output file
new_banner = json.load(open(f"_data/{files[0]}"))
print(new_banner)

# Update the existing file
json.dump(new_banner, open("banner.json", "w"))
