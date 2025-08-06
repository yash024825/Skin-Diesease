import os
import shutil
import pandas as pd

# Paths
DATASET_DIR_1 = "dataset/HAM10000_images_part_1"
DATASET_DIR_2 = "dataset/HAM10000_images_part_2"
METADATA_PATH = "dataset/HAM10000_metadata.csv"
OUTPUT_DIR = "dataset/ham10000_split"

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load metadata
df = pd.read_csv(METADATA_PATH)

# Map disease labels to readable names
label_map = {
    'akiec': 'Actinic_Keratoses',
    'bcc': 'Basal_Cell_Carcinoma',
    'bkl': 'Benign_Keratosis',
    'df': 'Dermatofibroma',
    'mel': 'Melanoma',
    'nv': 'Melanocytic_Nevus',
    'vasc': 'Vascular_Lesion'
}
df['dx'] = df['dx'].map(label_map)

# Copy images into class folders
for _, row in df.iterrows():
    img_name = row['image_id'] + ".jpg"
    label = row['dx']
    src_path = os.path.join(DATASET_DIR_1, img_name)
    if not os.path.exists(src_path):
        src_path = os.path.join(DATASET_DIR_2, img_name)

    if os.path.exists(src_path):
        dest_dir = os.path.join(OUTPUT_DIR, label)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.copy(src_path, os.path.join(dest_dir, img_name))

print("[INFO] Dataset split complete!")
