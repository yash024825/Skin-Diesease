from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
import numpy as np
import os
import json
from utils.preprocess import preprocess_image

app = Flask(__name__)
CORS(app)

# Load model & data
MODEL_PATH = os.path.join("model", "skin_disease_model.h5")
model = load_model(MODEL_PATH)
CLASS_LABELS = ['Eczema', 'Psoriasis', 'Melanoma', 'Acne', 'Normal']

with open("first_aid.json", "r") as f:
    first_aid_data = json.load(f)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    img = preprocess_image(file_path)
    prediction = model.predict(img)
    predicted_class = CLASS_LABELS[np.argmax(prediction)]
    confidence = float(np.max(prediction))
    first_aid = first_aid_data.get(predicted_class, "No data available.")

    return jsonify({
        "disease": predicted_class,
        "confidence": confidence,
        "first_aid": first_aid
    })

if __name__ == "__main__":
    app.run(debug=True)
