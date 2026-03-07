💳 Credit Card Fraud Detection System

A Beginner-Friendly Machine Learning Web Application: Python + Flask + Scikit-learn + MongoDB

📌 What This Project Teaches You

📌 What This Project Teaches You

🤖 **Machine Learning Model** – Detects fraudulent credit card transactions 
🌐 **Flask Backend Server** – Handles requests and connects the model with the web interface
🗄️ **MongoDB Database** – Stores transaction data and prediction results 
🎨 **Frontend** – Built using **HTML + CSS** for user interaction
🔄 Data Flow Example — Fraud Prediction

User enters transaction feature values in the web form

HTML form sends HTTP POST request → http://localhost:5000/predict

Flask backend receives the request and extracts the transaction features

Flask loads the trained machine learning model

The ML model analyzes the transaction data

The model predicts whether the transaction is:

Fraudulent 🚨
or
Normal Transaction ✅

Flask sends the prediction result back to the web page

The transaction data and prediction result are saved in MongoDB

🗂️ Project Structure
credit-card-fraud-detection/
│
├── model/
│   └── fraud_model.pkl        ← Trained Machine Learning Model
│
├── static/
│   └── style.css              ← CSS styling for web interface
│
├── templates/
│   └── index.html             ← User interface for input and results
│
├── train_model.py             ← Script to train the ML model
├── app.py                     ← Flask backend application
├── creditcard.csv             ← Dataset used for training
└── requirements.txt           ← List of required Python libraries

🚀 How to Run — Step by Step
STEP 1: Install Required Libraries

Open a terminal inside the project folder and run:

pip install -r requirements.txt

This installs the required libraries:

Flask

Pandas

NumPy

Scikit-learn

Joblib

PyMongo

STEP 2: Train the Machine Learning Model

Run the training script:

python train_model.py

This script will:

Load the credit card transaction dataset

Train a fraud detection model

Save the trained model as:

model/fraud_model.pkl
STEP 3: Start MongoDB Database

Start the MongoDB service:

net start MongoDB

MongoDB will store:

Transaction features

Prediction results

Transaction history

STEP 4: Run the Flask Application

Start the Flask backend server:

python app.py

You should see:

Running on http://127.0.0.1:5000
STEP 5: Open the Web Application

Open your browser and go to:

http://127.0.0.1:5000

Enter transaction feature values and click Predict.

The system will display:

Fraud Transaction 🚨
or
Normal Transaction ✅
✅ Test That Everything Works

Open the application in your browser:

http://127.0.0.1:5000

Enter transaction values and click Predict.

If everything works correctly:

The ML model predicts Fraud or Normal transaction

The result appears on the webpage

Transaction details are stored in MongoDB

🔍 Understanding the Key Concepts
What is Fraud Detection?

Fraud detection is the process of identifying suspicious or unauthorized financial transactions using machine learning algorithms.

Banks and financial institutions use similar systems to prevent financial fraud and financial losses.

What is a Machine Learning Model?

A machine learning model learns patterns from historical transaction data and predicts whether a new transaction is fraudulent or legitimate.

In this project, the model analyzes transaction features and classifies them into:

Fraud Transaction
or
Normal Transaction
What is Flask?

Flask is a Python web framework used to create web applications and APIs.

It connects the user interface with the machine learning model.

What is MongoDB?

MongoDB is a NoSQL database used to store:

Transaction data

Prediction results

User inputs

❓ Common Problems & Solutions

Model file not found

Run the training script first:

python train_model.py

MongoDB connection error

Make sure MongoDB is running:

net start MongoDB

Module not found error

Install the required libraries:

pip install -r requirements.txt
📚 What to Learn Next

Add prediction probability score

Create transaction history dashboard

Improve UI using Bootstrap or React

Deploy the project using Render / AWS / Heroku

Add user authentication and login system

