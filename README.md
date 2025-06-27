# 🌿 Plant Disease Detection and Cure Recommendation System

An AI-powered web application to detect plant diseases from leaf images using Convolutional Neural Networks (CNN) and suggest appropriate cures using agricultural medicines.

## 📌 Features

- 🌱 Upload plant leaf images through a simple web UI
- 🧠 Deep learning model (CNN) predicts disease among 38 classes
- 💊 Cure recommendation using specific fungicides/insecticides
- ⚡ Built with Flask for easy deployment and integration
- 📷 Real-time leaf image classification
- 🎯 Accuracy: **86–88%**

---

## 🛠️ Tech Stack

| Component       | Technology          |
|----------------|---------------------|
| Frontend       | HTML, CSS           |
| Backend        | Python, Flask       |
| Deep Learning  | TensorFlow, Keras   |
| Image Handling | PIL, NumPy          |
| Model          | Custom CNN (`model.h5`) |
| Deployment     | Localhost / Cloud-ready |

---

## 🧬 Disease Classes (Sample)

- Apple___Black_rot  
- Corn_(maize)___Common_rust_  
- Tomato___Leaf_Mold  
- Grape___Black_rot  
- Potato___Late_blight  
- _...38 classes total_

---

## 🩺 Cure Suggestions

Each prediction comes with a practical cure suggestion based on known treatments.

**Example:**  
- **Prediction:** `Tomato___Late_blight`  
- **Cure:** Spray **Ridomil Gold** (Metalaxyl + Mancozeb). Remove sick plants.

---
