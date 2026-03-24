import os
import json
import uuid
import numpy as np
import redis
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# -----------------------------------
# 🔹 Redis Connection
# -----------------------------------
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# -----------------------------------
# 🔹 Load Models
# -----------------------------------
cnn_model = load_model(os.path.join("h5_models", "CNN_model.h5"))
vgg_model = load_model(os.path.join("h5_models", "vgg16_model.h5"))
resnet_model = load_model(os.path.join("h5_models", "Resnet_model.h5"))

# -----------------------------------
# 🔹 Class Names
# -----------------------------------
class_names = [
    'apple_pie','Baked Potato','burger','butter_naan','chai','chapati','cheesecake',
    'chicken_curry','chole_bhature','Crispy Chicken','dal_makhani','dhokla','Donut',
    'fried_rice','Fries','Hot Dog','ice_cream','idli','jalebi','kaathi_rolls',
    'kadai_paneer','kulfi','masala_dosa','momos','omelette','paani_puri',
    'pakode','pav_bhaji','pizza','samosa','Sandwich','sushi','Taco','Taquito'
]

IMG_SIZE = 256

# -----------------------------------
# 🔹 Doctor Recommendation Dataset
# -----------------------------------
doctor_data = {

"pizza": ("Eat occasionally. High calories and cheese.", True),
"burger": ("Limit intake. Can increase cholesterol.", False),
"fried_rice": ("Safe if freshly cooked. Avoid excess oil.", True),
"Fries": ("Avoid frequent consumption. High trans fat.", False),
"ice_cream": ("Okay in moderation. High sugar.", True),
"samosa": ("Deep fried. Not good daily.", False),
"pav_bhaji": ("Fine occasionally but contains butter.", True),
"idli": ("Healthy and light food.", True),
"masala_dosa": ("Good but watch oil intake.", True),
"pakode": ("Deep fried snack. Eat rarely.", False),
"Sandwich": ("Usually safe depending on ingredients.", True),
"sushi": ("Healthy if fresh.", True),
"Taco": ("Moderate consumption recommended.", True),
"Taquito": ("Fried item. Avoid frequent intake.", False)

}

default_advice = ("Food is generally safe if prepared hygienically.", True)

# -----------------------------------
# 🔹 Home Route
# -----------------------------------
@app.route('/')
def home():
    return render_template("index.html", classes=class_names)

# -----------------------------------
# 🔹 Prediction Route
# -----------------------------------
@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['file']
    model_name = request.form['model_name']
    actual_class = request.form['actual_class']

    # -----------------------------------
    # 🔹 Save uploaded image
    # -----------------------------------
    upload_folder = os.path.join("static", "uploads")
    os.makedirs(upload_folder, exist_ok=True)

    unique_name = str(uuid.uuid4()) + "_" + file.filename
    filepath = os.path.join(upload_folder, unique_name)
    file.save(filepath)

    image_path = "/" + filepath

    # -----------------------------------
    # 🔹 Load Image
    # -----------------------------------
    img = image.load_img(filepath, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img)

    # -----------------------------------
    # 🔹 Model Selection
    # -----------------------------------
    if model_name == "cnn":
        model = cnn_model
        metrics_key = "CNN_matrix"
        img_array = img_array / 255.0

    elif model_name == "vgg16":
        model = vgg_model
        metrics_key = "vgg16_matrix"
        img_array = img_array / 255.0

    else:
        model = resnet_model
        metrics_key = "resnet_matrix"
        img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    # -----------------------------------
    # 🔹 Prediction
    # -----------------------------------
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = float(np.max(predictions)) * 100

    # -----------------------------------
    # 🔹 Get Nutrients using PREDICTED CLASS
    # -----------------------------------
    # -----------------------------------
    # 🔹 Get Nutrients using PREDICTED CLASS
    # -----------------------------------
    formatted_class = predicted_class.replace("_", " ").title()
    redis_key = f"food:{formatted_class}"

    food_json = r.get(redis_key)

    if food_json:
        properties = json.loads(food_json)
    else:
        properties = {}

    # -----------------------------------
    # 🔹 Model Metrics from Redis
    # -----------------------------------
    metrics_json = r.get(metrics_key)

    if metrics_json:
        metrics = json.loads(metrics_json)

        test_accuracy = metrics.get("test_accuracy", "N/A")

        if test_accuracy != "N/A":
            test_accuracy = round(float(test_accuracy) * 100, 2)

        class_metrics = metrics.get("classification_report", {})
        predicted_metrics = class_metrics.get(predicted_class, {})

        confusion_matrix = predicted_metrics.get("confusion_matrix", [])

        precision = round(predicted_metrics.get("precision", 0) * 100, 2)
        recall = round(predicted_metrics.get("recall", 0) * 100, 2)

    else:
        test_accuracy = "N/A"
        confusion_matrix = []
        precision = 0
        recall = 0

    # -----------------------------------
    # 🔹 Doctor Recommendation
    # -----------------------------------
    advice, safe = doctor_data.get(predicted_class, default_advice)

    # -----------------------------------
    # 🔹 Send Data to Frontend
    # -----------------------------------
    return render_template(
        "index.html",
        prediction=predicted_class,
        actual_class=actual_class,
        image_path=image_path,
        food_properties=properties,
        classes=class_names,
        test_accuracy=test_accuracy,
        confusion_matrix=confusion_matrix,
        precision=precision,
        recall=recall,
        model_name=model_name,
        doctor_advice=advice,
        is_safe=safe
    )

# -----------------------------------
# 🔹 Run App
# -----------------------------------
if __name__ == "__main__":
    app.run(debug=True)