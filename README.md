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
├── backend/                         # Python Flask Backend
│   ├── app.py                        # Flask API (predict endpoint)
│   ├── requirements.txt              # Backend dependencies
│   │
│   ├── model/                        # Trained ML Model
│   │   └── skin_disease_model.h5
│   │
│   ├── dataset/                      # Dataset Folder
│   │   ├── HAM10000_images_part_1/   # Original images (part 1)
│   │   ├── HAM10000_images_part_2/   # Original images (part 2)
│   │   ├── HAM10000_metadata.csv     # Metadata CSV
│   │   └── ham10000_split/           # Preprocessed dataset (train/test split)
│   │
│   ├── utils/                        # Helper functions
│   │   └── preprocess.py             # Preprocessing (resize, normalize, etc.)
│   │
│   ├── first_aid.json                # First aid guidance data
│   ├── train_model.py                # Model training script
│   └── split_ham10000.py             # Dataset split script
│
├── frontend/                         # React Frontend
│   ├── public/                       # Public assets
│   │   ├── index.html                # Main HTML
│   │   └── favicon.ico
│   │
│   ├── src/                          # React source files
│   │   ├── components/               # UI Components
│   │   │   ├── DiagnosisResult.js    # Shows diagnosis results
│   │   │   ├── ImageUpload.js        # Image upload form
│   │   │   └── Loader.js             # Loading spinner
│   │   │
│   │   ├── api.js                    # Axios / fetch API calls to Flask
│   │   ├── App.css                   # App styling
│   │   ├── App.js                    # Main App component
│   │   ├── App.test.js               # Unit tests
│   │   ├── index.css                 # Global CSS
│   │   ├── index.js                  # React entry point
│   │   ├── logo.svg                  # Logo
│   │   ├── reportWebVitals.js        # Performance report
│   │   └── setupTests.js             # Testing setup
│   │
│   ├── package.json                  # Frontend dependencies
│   ├── package-lock.json
│   └── README.md                     # Frontend-specific instructions
│
├── .gitignore                        # Git ignore file
└── README.md                         # Main Project README

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
git clone https://github.com/your-username/skin-disease-diagnosis.git
cd skin-disease-diagnosis

###🔹 2. Backend Setup (Flask + TensorFlow)

#Navigate to the backend folder:

cd backend


#Create and activate a virtual environment:

python -m venv venv


#Windows:

venv\Scripts\activate


#Linux/Mac:

source venv/bin/activate


#Install required dependencies:

pip install -r requirements.txt


#(Optional) Train the model again:

python train_model.py


#Start the Flask server:

python app.py


✅ Backend will run at: http://127.0.0.1:5000

🔹 3. Frontend Setup (React.js)

Open a new terminal and navigate to the frontend folder:

cd frontend


Install dependencies:

npm install


Start the React development server:

npm start


✅ Frontend will run at: http://localhost:3000

🔹 4. Connecting Frontend & Backend

Make sure the Flask backend is running on port 5000.

The React frontend will call backend APIs like:

const response = await fetch("http://127.0.0.1:5000/predict", {
  method: "POST",
  body: formData
});

🧪 Example API Endpoint

POST /predict

Request: Upload image file

Response:

{
  "disease": "Melanoma",
  "confidence": 0.92,
  "first_aid": "Consult a dermatologist immediately..."
}

📊 Dataset

HAM10000 (Human Against Machine with 10000 training images)

Source: Kaggle HAM10000 Dataset

Classes include: Melanocytic nevi, Melanoma, Benign keratosis, Basal cell carcinoma, etc.

🚀 Tech Stack

Frontend: React.js, Tailwind CSS

Backend: Flask (Python)

AI Model: TensorFlow / Keras (CNN)

Dataset: HAM10000

Image Processing: OpenCV, Pillow
