import pandas as pd
import os
import shutil

# CSV path
csv_file_path = 'C:/Users/...'

# photo location
original_photo_dir = 'C:/Users/...'
new_photo_dir = 'C:/Users/...'

# Ensure the new directory exists
if not os.path.exists(new_photo_dir):
    os.makedirs(new_photo_dir)

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Iterate through the DataFrame
for index, row in df.iterrows():
    original_file_name = str(row['name']) + '.jpg'
    new_file_name = str(row['personal code']) + '.jpg'

    original_file_path = os.path.join(original_photo_dir, original_file_name)
    new_file_path = os.path.join(new_photo_dir, new_file_name)

    # Check if the original file exists and then copy and rename
    if os.path.exists(original_file_path):
        shutil.copy2(original_file_path, new_file_path)
        print(f"Copied and renamed: {original_file_path} to {new_file_path}")
    else:
        print(f"File not found: {original_file_path}")

print("Renaming completed.")