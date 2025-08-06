import React from "react";

function ImageUploader({ setFile, onUpload }) {
  return (
    <div>
      <input type="file" accept="image/*" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={onUpload}>Upload & Diagnose</button>
    </div>
  );
}

export default ImageUploader;
