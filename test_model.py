import os
from pathlib import Path
from ultralytics import YOLO
import cv2

# --- CONFIGURATION ---
IMAGE_FOLDER = r"C:\Users\ThinkPad\Downloads\Zakaria1"           # Folder containing images
MODEL_PATH = "plate.pt"  # Your YOLO model
CLASS_ID = 0                      # Assuming plate is class 0

# --- LOAD MODEL ---
model = YOLO(MODEL_PATH)

# --- PROCESS IMAGES ---
image_paths = list(Path(IMAGE_FOLDER).glob("*.[jp][pn]g"))  # jpg, jpeg, png
for img_path in image_paths:
    img = cv2.imread(str(img_path))
    height, width = img.shape[:2]

    # Detect plates
    results = model(img, verbose=False)[0]

    # Prepare output
    label_path = img_path.with_suffix(".txt")
    with open(label_path, "w") as f:
        for box in results.boxes:
            cls_id = int(box.cls.item())
            if cls_id != CLASS_ID:
                continue

            x1, y1, x2, y2 = box.xyxy[0]
            x_center = ((x1 + x2) / 2) / width
            y_center = ((y1 + y2) / 2) / height
            w = (x2 - x1) / width
            h = (y2 - y1) / height

            f.write(f"{cls_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

    print(f"[✓] Saved: {label_path.name}")

print("\n✅ All detections completed.")
