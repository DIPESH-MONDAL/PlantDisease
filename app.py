from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model("model.h5")

# Class names
class_names = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___healthy",
    "Blueberry___healthy", "Cherry_(including_sour)___healthy", "Cherry_(including_sour)___Powdery_mildew",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", "Corn_(maize)___Common_rust_", "Corn_(maize)___healthy",
    "Corn_(maize)___Northern_Leaf_Blight", "Grape___Black_rot", "Grape___Esca_(Black_Measles)",
    "Grape___healthy", "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot", "Peach___healthy", "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy",
    "Potato___Early_blight", "Potato___healthy", "Potato___Late_blight", "Raspberry___healthy",
    "Soybean___healthy", "Squash___Powdery_mildew", "Strawberry___healthy", "Strawberry___Leaf_scorch",
    "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___healthy", "Tomato___Late_blight",
    "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot", "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot", "Tomato___Tomato_mosaic_virus", "Tomato___Tomato_Yellow_Leaf_Curl_Virus"
]

# Cure dictionary
cure_dict = {
    "Apple___Apple_scab": "Spray medicine like Mancozeb (e.g., Dithane M-45) and remove all infected or damaged leaves.",
    "Apple___Black_rot": "Cut black or rotten branches. Spray Carbendazim (e.g., Bavistin) to protect the plant.",
    "Apple___Cedar_apple_rust": "Remove nearby cedar trees. Spray Hexaconazole or Mancozeb-based fungicide.",
    "Apple___healthy": "Plant is healthy. No treatment needed.",
    "Blueberry___healthy": "Plant is healthy. No treatment needed.",
    "Cherry_(including_sour)___healthy": "Plant is healthy. No treatment needed.",
    "Cherry_(including_sour)___Powdery_mildew": "Cut off white powdery leaves and spray Sulfur-based fungicide (e.g., Sulfex).",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "Use resistant seeds. Spray Mancozeb or Zineb and rotate crops yearly.",
    "Corn_(maize)___Common_rust_": "Grow strong seed varieties. Spray Propiconazole (e.g., Tilt) if disease spreads.",
    "Corn_(maize)___healthy": "Plant is healthy. No treatment needed.",
    "Corn_(maize)___Northern_Leaf_Blight": "Use hybrid seeds and spray Mancozeb or Carbendazim for leaf protection.",
    "Grape___Black_rot": "Spray Mancozeb (e.g., Dithane M-45) and remove dried, infected grapes (mummies).",
    "Grape___Esca_(Black_Measles)": "Avoid cutting during rain. Remove affected wood and apply Copper Oxychloride on wounds.",
    "Grape___healthy": "Plant is healthy. No treatment needed.",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": "Spray Chlorothalonil (e.g., Kavach) and remove sick leaves.",
    "Orange___Haunglongbing_(Citrus_greening)": "Use healthy seedlings. Control psyllid insects with Imidacloprid (e.g., Confidor).",
    "Peach___Bacterial_spot": "Spray Copper Oxychloride (e.g., Blitox) and use resistant peach varieties.",
    "Peach___healthy": "Plant is healthy. No treatment needed.",
    "Pepper,_bell___Bacterial_spot": "Use clean seeds. Spray Copper Hydroxide or Copper Oxychloride.",
    "Pepper,_bell___healthy": "Plant is healthy. No treatment needed.",
    "Potato___Early_blight": "Spray Mancozeb or Chlorothalonil and rotate crops to prevent spread.",
    "Potato___healthy": "Plant is healthy. No treatment needed.",
    "Potato___Late_blight": "Spray Metalaxyl + Mancozeb combo (e.g., Ridomil Gold) and remove infected plants.",
    "Raspberry___healthy": "Plant is healthy. No treatment needed.",
    "Soybean___healthy": "Plant is healthy. No treatment needed.",
    "Squash___Powdery_mildew": "Spray Sulfur-based or systemic fungicides like Tebuconazole (e.g., Folicur).",
    "Strawberry___healthy": "Plant is healthy. No treatment needed.",
    "Strawberry___Leaf_scorch": "Remove infected leaves. Give enough space for air. Spray Mancozeb if needed.",
    "Tomato___Bacterial_spot": "Use certified seeds and spray Copper Oxychloride (e.g., Blitox 50).",
    "Tomato___Early_blight": "Spray Chlorothalonil or Mancozeb. Avoid watering from above.",
    "Tomato___healthy": "Plant is healthy. No treatment needed.",
    "Tomato___Late_blight": "Remove sick plants. Spray Ridomil Gold (Metalaxyl + Mancozeb).",
    "Tomato___Leaf_Mold": "Allow air to flow. Spray fungicide like Azoxystrobin (e.g., Amistar).",
    "Tomato___Septoria_leaf_spot": "Remove affected leaves. Spray Mancozeb or Copper fungicide.",
    "Tomato___Spider_mites Two-spotted_spider_mite": "Spray Neem oil or use Miticides like Abamectin (e.g., Vertimec).",
    "Tomato___Target_Spot": "Spray Chlorothalonil or Mancozeb and rotate crops each season.",
    "Tomato___Tomato_mosaic_virus": "Remove and burn infected plants. Clean tools with bleach solution.",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "Spray Imidacloprid (e.g., Confidor) to control whiteflies. Use resistant seeds."
}

# Image preprocessing
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict_route():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_bytes = request.files['image'].read()
    preprocessed = preprocess_image(image_bytes)
    prediction = model.predict(preprocessed)
    class_idx = np.argmax(prediction)
    result = class_names[class_idx]
    cure = cure_dict.get(result, "No cure information available.")

    return jsonify({'prediction': result, 'cure': cure})

# HTML UI route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
