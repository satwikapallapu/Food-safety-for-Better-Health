🥗 Food Safety for Better Health

An end-to-end AI-powered web application that classifies food images, provides nutritional insights, and offers health-based recommendations using Deep Learning.

🚀 Project Overview

This project focuses on building an intelligent Food Classification and Safety Analysis System using Deep Learning techniques.

The system is designed to:

Classify food images into 34 categories
Provide nutritional information
Generate doctor-based recommendations
Display model performance metrics
Support multiple deep learning models
🧠 Models Used
Custom CNN
VGG16
ResNet50

All models were trained using Google Colab and integrated into a Flask-based web application.

📊 Dataset Details
34 Food Classes
Training: 200 images per class
Validation: 50 images per class
Testing: 10 images per class
🍽️ Classes Include:

apple_pie, Baked Potato, burger, butter_naan, chai, chapati, cheesecake, chicken_curry, chole_bhature, Crispy Chicken, dal_makhani, dhokla, Donut, fried_rice, Fries, Hot Dog, ice_cream, idli, jalebi, kaathi_rolls, kadai_paneer, kulfi, masala_dosa, momos, omelette, paani_puri, pakode, pav_bhaji, pizza, samosa, Sandwich, sushi, Taco, Taquito

🧾 Nutritional Information

Each food item includes:

Calories (kcal)
Total Fat
Saturated Fat
Trans Fat
Cholesterol
Sodium
Carbohydrates
Dietary Fiber
Sugars
Protein
Vitamin C
Calcium
Iron
Potassium

Stored in a JSON file and retrieved dynamically using Redis.

⚙️ Tech Stack
🔹 Backend
Python
Flask
TensorFlow / Keras
NumPy
🔹 Frontend
HTML
CSS (Bootstrap)
JavaScript
🔹 Database / Storage
Redis
Model metrics
Nutritional data
🔁 System Workflow
User uploads a food image
Selects model (CNN / VGG16 / ResNet50)
Image preprocessing is performed
Model predicts the food class
System:
Fetches nutrients from Redis
Retrieves model performance metrics
Generates doctor recommendation
Results are displayed on the web interface
📈 Model Evaluation Metrics

The system tracks and displays:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix

All metrics are stored and fetched dynamically using Redis.

🩺 Doctor Recommendation System
Provides health advice based on predicted food
Indicates whether food is safe or not safe
Helps users make informed dietary decisions
💻 Web Application Features
Upload food image
Select model for prediction
Real-time classification
Nutritional breakdown
Doctor recommendation
Model performance visualization
📁 Project Structure
Food-Safety-App/
│
├── h5_models/                # Trained Deep Learning Models
│   ├── CNN_model.h5
│   ├── Resnet_model.h5
│   └── vgg16_model.h5
│
├── models/                   # Model Evaluation Metrics
│   ├── CNN_matrix.json
│   ├── resnet_matrix.json
│   └── vgg16_matrix.json
│
├── static/                   # Static files
│   ├── uploads/              # Uploaded images
│   └── img.jpg               # Profile image
│
├── templates/                # Frontend HTML
│   └── index.html
│
├── app.py                    # Main Flask backend
├── cnn.py                    # CNN logic / training
├── food.json.py              # JSON handling
├── food_data.json            # Nutritional dataset
├── main.py                   # Entry script
│
├── .venv/                    # Virtual environment
└── README.md

⚡ Redis is used to store model metrics and food nutritional data for fast retrieval.

📌 Sample Output
Predicted Food : Donut  
Confidence     : 92%  
Calories       : 270 kcal  
Protein        : 4g  
Health Status  : Doctor Recommended  

💡 The system not only predicts the food item but also provides nutritional insights and health recommendations.


🏁 Conclusion

This project demonstrates the practical application of Deep Learning in solving real-world problems related to food and health. By combining image classification, nutritional analysis, and intelligent recommendations, the system provides a complete AI-driven solution for smarter dietary decisions.

It highlights the integration of multiple models, efficient data handling using Redis, and deployment through a user-friendly web interface. Overall, this project strengthened my skills in Machine Learning, Deep Learning, model deployment, and full-stack development.

👩‍💻 Author
Pallapu Sathwika 
AI & ML Intern
- 🔗 LinkedIn: www.linkedin.com/in/sathwika-pallapu-a32bba355  
