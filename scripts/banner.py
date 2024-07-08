import json
import os
import re

if not os.path.exists("_data"):
    os.makedirs("_data")

files = os.listdir("_data")
print(files)

if not files:
    raise FileNotFoundError("No files found in _data directory")

issue_data = json.load(open(f"_data/{files[0]}"))
print(issue_data)

body = issue_data.get("body", "")
banner_text = re.search(r'### Banner Text\s*([\s\S]*?)\r?\n\r?\n', body)
expires_on = re.search(r'### Expires On\s*([\s\S]*?)\r?\n\r?\n', body)
link = re.search(r'### Link\s*([\s\S]*?)\r?\n\r?\n', body)

banner_text = banner_text.group(1).strip() if banner_text else ""
expires_on = expires_on.group(1).strip() if expires_on else ""
link = link.group(1).strip() if link else ""


new_banner = {
    "text": banner_text,
    "link": link,
    "expires_on": expires_on
}

# Write the new banner JSON to the output file
with open("banner.json", "w") as outfile:
    json.dump(new_banner, outfile, indent=2)

print("Updated banner.json content:", new_banner)
