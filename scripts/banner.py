# import json
# import os
#
# # Get the output file
# if not os.path.exists("_data"):
#     os.makedirs("_data")
#
# files = os.listdir("_data")
# print(files)
# # Read the output file
# new_banner = json.load(open(f"_data/{files[0]}"))
# print(new_banner)
#
# # Update the existing file
# json.dump(new_banner, open("banner.json", "w"))
import json
import os

# Ensure the directory exists
if not os.path.exists("_data"):
    os.makedirs("_data")

# Get the output file
files = os.listdir("_data")
print(files)

if not files:
    raise FileNotFoundError("No files found in _data directory")

# Read the output file
new_banner = json.load(open(f"_data/{files[0]}"))
print(new_banner)

# Update the existing file
json.dump(new_banner, open("banner.json", "w"))
