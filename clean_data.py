import os
import shutil

# Paths (customize these)
image_folder = r"D:\akwa\salaheddine"
label_folder = r"D:\akwa\salaheddine"
output_folder = r"D:\akwa\images"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported image extensions
image_exts = (".jpg", ".jpeg", ".png", ".bmp")

# Loop through images
for filename in os.listdir(image_folder):
    if filename.lower().endswith(image_exts):
        name_without_ext = os.path.splitext(filename)[0]
        label_file = os.path.join(label_folder, name_without_ext + ".txt")

        if os.path.exists(label_file):
            src_path = os.path.join(image_folder, filename)
            dst_path = os.path.join(output_folder, filename)
            shutil.copy2(src_path, dst_path)

print("Done. Labeled images copied to:", output_folder)
