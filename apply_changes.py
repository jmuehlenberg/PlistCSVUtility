import os
import plistlib
import csv

def unflatten_dict(d, sep='.'):
    items = {}
    for k, v in d.items():
        keys = k.split(sep)
        sub_dict = items
        for sub_key in keys[:-1]:
            sub_dict = sub_dict.setdefault(sub_key, {})
        sub_dict[keys[-1]] = v
    return items

# Define the directory path and input CSV file
dir_path = os.path.expanduser('~/Library/AutoPkg/RecipeOverridesTest/')
input_csv_path = os.path.expanduser('~/Desktop/all_values.csv')

# Read the CSV file
with open(input_csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    collected_data = {}
    for row in csvreader:
        pkg, key, value = row
        if pkg not in collected_data:
            collected_data[pkg] = {}
        collected_data[pkg][key] = value

# Update the plist files
for pkg, flat_data in collected_data.items():
    full_path = os.path.join(dir_path, pkg)
    if os.path.exists(full_path):
        # Read the existing plist file
        with open(full_path, 'rb') as fp:
            plist_data = plistlib.load(fp)

        # Update the plist data
        update_data = unflatten_dict(flat_data)
        plist_data.update(update_data)
