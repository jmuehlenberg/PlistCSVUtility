import os
import plistlib
import csv

def flatten_dict(d, parent_key='', sep='.'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

# Define the directory path and output CSV file
dir_path = os.path.expanduser('~/Library/AutoPkg/RecipeOverridesTest/')
output_csv_path = os.path.expanduser('~/Desktop/all_values.csv')

# Prepare to write to the CSV file
with open(output_csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['PKG', 'KEY', 'VALUE'])  # Write header row

    # Iterate through the files in the directory
    for filename in os.listdir(dir_path):
        if filename.endswith('.recipe'):
            full_path = os.path.join(dir_path, filename)

            # Read the plist file
            with open(full_path, 'rb') as fp:
                plist_data = plistlib.load(fp)

            # Flatten the plist dictionary
            flat_data = flatten_dict(plist_data)

            # Write to the CSV file
            for key, value in flat_data.items():
                csvwriter.writerow([filename, key, value])

print(f"All values written to {output_csv_path}")
