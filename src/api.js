import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000" // Flask backend URL
});

export const predictDisease = (formData) =>
  API.post("/predict", formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });
