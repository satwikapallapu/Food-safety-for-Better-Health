<h1 align="left">🥗 Food Safety for Better Health</h1>

<p align="center">
An AI-powered web application that classifies food images, provides nutritional insights, and gives health recommendations using Deep Learning.
</p>

<hr>

<h2>🚀 Project Overview</h2>
<p>
This project is an end-to-end <b>Food Classification and Safety Analysis System</b> built using Deep Learning.
It classifies food images, provides nutritional values, and generates doctor recommendations.
</p>

<ul>
<li>🍽️ Classifies <b>34 food categories</b></li>
<li>📊 Provides nutritional insights</li>
<li>🩺 Gives doctor recommendations</li>
<li>📈 Displays model performance metrics</li>
<li>🤖 Supports multiple DL models</li>
</ul>

<hr>

<h2>🧠 Models Used</h2>
<ul>
<li>Custom CNN</li>
<li>VGG16</li>
<li>ResNet50</li>
</ul>

<hr>

<h2>📊 Dataset Details</h2>
<ul>
<li><b>34 Classes</b></li>
<li>Training: 200 images/class</li>
<li>Validation: 50 images/class</li>
<li>Testing: 10 images/class</li>
</ul>

<p><b>Sample Classes:</b> apple_pie, burger, idli, pizza, samosa, sushi, momos, pav_bhaji...</p>

<hr>

<h2>🧾 Nutritional Information</h2>
<p>Each food item includes:</p>
<ul>
<li>Calories, Fat, Cholesterol</li>
<li>Carbohydrates, Fiber, Sugars</li>
<li>Protein</li>
<li>Vitamins & Minerals</li>
</ul>

<p>Stored in JSON and retrieved using <b>Redis</b>.</p>

<hr>

<h2>⚙️ Tech Stack</h2>

<h3>Backend</h3>
<ul>
<li>Python</li>
<li>Flask</li>
<li>TensorFlow / Keras</li>
<li>NumPy</li>
</ul>

<h3>Frontend</h3>
<ul>
<li>HTML</li>
<li>CSS (Bootstrap)</li>
<li>JavaScript</li>
</ul>

<h3>Database</h3>
<ul>
<li>Redis (for metrics & nutrients)</li>
</ul>

<hr>

<h2>🔁 System Workflow</h2>
<ol>
<li>Upload image</li>
<li>Select model (CNN / VGG16 / ResNet50)</li>
<li>Image preprocessing</li>
<li>Prediction</li>
<li>Fetch nutrients & metrics from Redis</li>
<li>Display results</li>
</ol>

<hr>

<h2>📈 Model Evaluation</h2>
<ul>
<li>Accuracy</li>
<li>Precision</li>
<li>Recall</li>
<li>F1-Score</li>
<li>Confusion Matrix</li>
</ul>

<hr>

<h2>🩺 Doctor Recommendation</h2>
<p>
The system provides health advice based on predicted food and indicates whether it is safe or not.
</p>

<hr>

<h2>💻 Features</h2>
<ul>
<li>Image upload</li>
<li>Multi-model selection</li>
<li>Real-time prediction</li>
<li>Nutritional breakdown</li>
<li>Doctor advice</li>
<li>Performance metrics display</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
Food-Safety-App/
│
├── h5_models/
│   ├── CNN_model.h5
│   ├── Resnet_model.h5
│   └── vgg16_model.h5
│
├── models/
│   ├── CNN_matrix.json
│   ├── resnet_matrix.json
│   └── vgg16_matrix.json
│
├── static/
│   ├── uploads/
│   └── sathwika.jpg
│
├── templates/
│   └── index.html
│
├── app.py
├── cnn.py
├── food.json.py
├── food_data.json
├── main.py
│
├── .venv/
└── README.md
</pre>

<p><i>Redis is used to store model metrics and nutritional data for faster access.</i></p>

<hr>

<h2>📌 Sample Output</h2>

<pre>
Predicted Food : Donut  
Confidence     : 92%  
Calories       : 270 kcal  
Protein        : 4g  
Health Status  : Doctor Recommended  
</pre>

<hr>

<h2>▶️ How to Run</h2>

<pre>
git clone https://github.com/your-username/food-safety-app.git
cd food-safety-app
pip install -r requirements.txt
python app.py
</pre>

<p>Make sure Redis is running at: <b>localhost:6379</b></p>

<hr>

<h2>🌟 Key Highlights</h2>
<ul>
<li>Multi-model comparison</li>
<li>Real-time predictions</li>
<li>Redis integration</li>
<li>AI + Nutrition + Health</li>
</ul>

<hr>

<h2>🚀 Future Improvements</h2>
<ul>
<li>Increase dataset size</li>
<li>Add more food categories</li>
<li>Cloud deployment</li>
<li>Better UI/UX</li>
</ul>

<hr>

<h2>🏁 Conclusion</h2>
<p>
This project demonstrates the real-world application of Deep Learning in food and health analysis.
By combining image classification, nutrition tracking, and intelligent recommendations,
it provides a complete AI-driven solution for better dietary decisions.
</p>

<hr>

<h2>👩‍💻 Author</h2>

<p><b>Pallapu SAthwika </b><br>
AI & ML Intern</p>


<p>
🔗 LinkedIn: www.linkedin.com/in/sathwika-pallapu-a32bba355 <br>
</p>
