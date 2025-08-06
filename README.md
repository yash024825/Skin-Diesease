# 🩺 AI-Based Skin Condition Diagnosis

An AI-powered web application that detects skin diseases from images using a **React.js frontend**, a **Flask (Python) backend**, and a **TensorFlow deep learning model** trained on the **HAM10000 dataset**.  
The system provides early diagnosis and first aid guidance for common skin conditions.

---

## 📌 Features
- Upload a skin image from the web interface.
- AI model predicts the disease type with high accuracy.
- Displays disease name and confidence score.
- Provides **first aid tips** for the detected condition.
- Uses **memory-efficient training** to handle large datasets.
- Modern and responsive **React.js UI**.

---

## 🏗 Project Structure
skin-disease-diagnosis/
│
├── backend/ # Python Flask Backend
│ ├── app.py # Flask API
│ ├── model/
│ │ └── skin_disease_model.h5 # Trained ML model
│ ├── dataset/
│ │ ├── HAM10000_images_part_1/ # Original dataset part 1
│ │ ├── HAM10000_images_part_2/ # Original dataset part 2
│ │ ├── HAM10000_metadata.csv # Metadata with labels
│ │ └── ham10000_split/ # Organized dataset by class
│ ├── utils/
│ │ └── preprocess.py # Image preprocessing
│ ├── first_aid.json # First aid tips
│ ├── requirements.txt # Python dependencies
│ ├── train_model.py # Model training script
│ └── split_ham10000.py # Dataset preparation script
│
├── frontend/ # React.js Frontend
│ ├── public/
│ └── src/
│
└── README.md

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/skin-disease-diagnosis.git
cd skin-disease-diagnosis
