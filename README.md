# PlistCSVUtility
A utility for macOS that allows administrators to extract values from AutoPkg RecipeOverride plist files to a CSV, make changes, and then apply those changes back to the plist files.

## Features

- **Extract Information**: `get_overrides.py` will scan through plist files and export keys and values to a CSV file.
- **Apply Changes**: `apply_changes.py` will read a modified CSV file and update the plist files accordingly.
- **Flexible**: You can add lines to the CSV file for keys that may not exist in the original plist. These keys and values will be added to the plist files when you run `apply_changes.py`.

## Requirements

- Python 3.x
- `plistlib` library

You can install any missing libraries using pip:
```
pip install plistlib
```

## How to Use

1. **Extract Information**

    Run `get_overrides.py` to generate a CSV file with keys and values from plist files.
    ```bash
    python3 get_overrides.py
    ```

    This will generate a CSV file on your Desktop named `all_values.csv`.

2. **Modify CSV**

    Open `all_values.csv` with Apple Numbers or any other CSV editor. Modify the values as you see fit. You can even add new lines for keys that you want to add to the plist files.

3. **Apply Changes**

    After editing the CSV, save it and run `apply_changes.py` to apply the changes to the plist files.
    ```bash
    python3 apply_changes.py
    ```

    This will read the modified `all_values.csv` file and update or add keys and values to the plist files.

## Important Note

- The scripts are designed to read from and write to `~/Library/AutoPkg/RecipeOverrides/`. Please make sure you have the necessary permissions or change the path.
