import os
import re

def remove_copied_images_by_name(folder_path):
    pattern = re.compile(r"^(.*)\s\(\d+\)(\.\w+)$")  # Matches filenames like "name (1).jpg"
    deleted_files = []

    for filename in os.listdir(folder_path):
        match = pattern.match(filename)
        if match:
            full_path = os.path.join(folder_path, filename)
            os.remove(full_path)
            deleted_files.append(filename)
            print(f"Deleted: {filename}")

    print(f"\n✅ {len(deleted_files)} copied images deleted.")

# Replace with your actual folder path
folder = r"C:\Users\ThinkPad\Downloads\Verification\mouad"
remove_copied_images_by_name(folder)
