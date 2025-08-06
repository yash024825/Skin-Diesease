import React from "react";

function DiagnosisResult({ result }) {
  return (
    <div>
      <h3>Disease: {result.disease}</h3>
      <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
      <p>First Aid: {result.first_aid}</p>
    </div>
  );
}

export default DiagnosisResult;
