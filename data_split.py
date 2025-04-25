import os
import random
import shutil

# Paths
base_dir = r"D:\akwa\dataset"
images_dir = os.path.join(base_dir, "images")
labels_dir = os.path.join(base_dir, "labels")

train_images_dir = os.path.join(base_dir, "images/train")
val_images_dir = os.path.join(base_dir, "images/val")
train_labels_dir = os.path.join(base_dir, "labels/train")
val_labels_dir = os.path.join(base_dir, "labels/val")

# Create target directories
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# List all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Shuffle and select 400 for validation
random.shuffle(image_files)
val_images = image_files[:400]
train_images = image_files[400:]

# Move images and corresponding labels
def move_files(file_list, src_img_dir, src_lbl_dir, dest_img_dir, dest_lbl_dir):
    for img_file in file_list:
        label_file = os.path.splitext(img_file)[0] + ".txt"
        
        shutil.move(os.path.join(src_img_dir, img_file), os.path.join(dest_img_dir, img_file))
        shutil.move(os.path.join(src_lbl_dir, label_file), os.path.join(dest_lbl_dir, label_file))

# Perform the move
move_files(val_images, images_dir, labels_dir, val_images_dir, val_labels_dir)
move_files(train_images, images_dir, labels_dir, train_images_dir, train_labels_dir)

print("Split completed: 400 images moved to 'val', remaining to 'train'.")
