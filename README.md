#🌿 Plant Disease Detection and Cure Recommendation System
An AI-powered web application to detect plant diseases from leaf images using Convolutional Neural Networks (CNN) and suggest appropriate cures using agricultural medicines.

📌 Features
🌱 Upload plant leaf images through a simple web UI

🧠 Deep learning model (CNN) predicts disease among 38 classes

💊 Cure recommendation using specific fungicides/insecticides

⚡ Built with Flask for easy deployment and integration

📷 Real-time leaf image classification

🎯 Accuracy: 86–88%

🚀 Demo

🛠️ Tech Stack
Component	Technology
Frontend	HTML, CSS
Backend	Python, Flask
Deep Learning	TensorFlow, Keras
Image Handling	PIL, NumPy
Model	Custom CNN (saved as model.h5)
Deployment	Localhost / Cloud-ready

🧬 Disease Classes (Sample)
Apple___Black_rot

Corn_(maize)__Common_rust

Tomato___Leaf_Mold

Grape___Black_rot

Potato___Late_blight

... (total 38 classes)

🩺 Cure Suggestions
Each prediction comes with a practical cure suggestion based on known treatments. Example:

Prediction: Tomato___Late_blight

Cure: Spray Ridomil Gold (Metalaxyl + Mancozeb). Remove sick plants.

📁 Project Structure
csharp
Copy
Edit
plant-disease-detection/
│
├── app.py                # Flask backend
├── model.h5              # Trained CNN model
├── templates/
│   └── index.html        # Upload form UI
├── static/               # CSS / JS / assets (optional)
├── plantdisease_with_flask.ipynb  # Model training notebook
├── README.md             # Project info
▶️ How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/plant-disease-detection.git
cd plant-disease-detection
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000/
🔍 Sample Use
Upload an image of a plant leaf.

The model predicts the disease.

The system returns:

Disease name

Cure recommendation

📈 Accuracy & Performance
Achieved 86–88% accuracy on test data

Evaluated with standard metrics (accuracy, precision)

Real-time predictions under 1 second

🧠 Future Enhancements
📱 Mobile-friendly frontend or Android app

📡 Live agri-expert chat integration

🗣️ Voice-based guidance for illiterate farmers

🌍 Multilingual support (Hindi, Odia, Bengali, etc.)

🔗 Offline model via TensorFlow Lite

📚 Dataset
Source: PlantVillage Dataset
https://www.tensorflow.org/datasets/catalog/plant_village

👥 Authors
Dipesh Mondal
GitHub | LinkedIn

📜 License
This project is open-source and available under the MIT License.
