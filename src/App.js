import React, { useState } from "react";
import { predictDisease } from "./api";
import ImageUploader from "./components/ImageUploader";
import DiagnosisResult from "./components/DiagnosisResult";
import Loader from "./components/Loader";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first.");
      return;
    }
    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await predictDisease(formData);
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error in prediction");
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>AI-Based Skin Condition Diagnosis</h1>
      <ImageUploader setFile={setFile} onUpload={handleUpload} />
      {loading && <Loader />}
      {result && <DiagnosisResult result={result} />}
    </div>
  );
}

export default App;
