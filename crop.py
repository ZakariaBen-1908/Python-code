import os
from PIL import Image

# Dossiers à modifier selon ton arborescence
input_folder = r"D:\akwa\cameras20F"
output_folder = r"D:\akwa\cam20f"

# Créer le dossier de sortie s’il n’existe pas
os.makedirs(output_folder, exist_ok=True)

# Coordonnées des deux zones à découper
crop_box_1 = (160, 62, 990, 1044)
crop_box_2 = (990, 62, 1850, 1044)

# Traitement des images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        input_path = os.path.join(input_folder, filename)

        # Nom de fichier sans extension
        base_name = os.path.splitext(filename)[0]

        with Image.open(input_path) as img:
            img = img.convert("RGB")

            # Zone 1
            cropped_img1 = img.crop(crop_box_1)
            output_path1 = os.path.join(output_folder, base_name + "_zone1.jpg")
            cropped_img1.save(output_path1, format="JPEG", quality=95)

            # Zone 2
            cropped_img2 = img.crop(crop_box_2)
            output_path2 = os.path.join(output_folder, base_name + "_zone2.jpg")
            cropped_img2.save(output_path2, format="JPEG", quality=95)

print("Toutes les images ont été recadrées sur 2 zones et sauvegardées en JPG dans :", output_folder)