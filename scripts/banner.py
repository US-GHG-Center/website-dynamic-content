# import json
# import os
#
# # Ensure the directory exists
# if not os.path.exists("_data"):
#     os.makedirs("_data")
#
# # Get the output file
# files = os.listdir("_data")
# print(files)
#
# if not files:
#     raise FileNotFoundError("No files found in _data directory")
#
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

# Read the input JSON file
issue_data = json.load(open(f"_data/{files[0]}"))
print(issue_data)

# Extract the necessary fields from the issue body
body_lines = issue_data["body"].split('\r\n')
banner_text = ''
expires_on = ''
link = ''

for i in range(len(body_lines)):
    if '### Banner Text' in body_lines[i]:
        banner_text = body_lines[i+1].strip()
    elif '### Expires On' in body_lines[i]:
        expires_on = body_lines[i+1].strip()
    elif '### Link' in body_lines[i]:
        link = body_lines[i+1].strip()

# Create the new banner JSON structure
new_banner = {
    "text": banner_text,
    "link": link,
    "expires_on": expires_on
}

# Write the new banner JSON to the output file
with open("banner.json", "w") as outfile:
    json.dump(new_banner, outfile, indent=2)

print("Updated banner.json content:", new_banner)
