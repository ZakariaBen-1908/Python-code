import os
import shutil
import random

def split_images(input_folder, output_root, num_splits=6):
    # Get all image filenames
    all_images = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff'))]
    
    # Shuffle the images randomly
    random.shuffle(all_images)

    # Calculate split size
    split_size = len(all_images) // num_splits
    remainder = len(all_images) % num_splits  # Extra images to distribute

    start = 0
    for i in range(num_splits):
        end = start + split_size + (1 if i < remainder else 0)
        split_images = all_images[start:end]

        # Create split folder
        split_folder = os.path.join(output_root, f"split_{i+1}")
        os.makedirs(split_folder, exist_ok=True)

        # Copy images to split folder
        for img_file in split_images:
            src = os.path.join(input_folder, img_file)
            dst = os.path.join(split_folder, img_file)
            shutil.copy2(src, dst)

        print(f"Split {i+1}: {len(split_images)} images -> {split_folder}")
        start = end

# Example usage:
input_folder = "your_input_images_folder"
output_root = "output_splits"

split_images(input_folder, output_root)
