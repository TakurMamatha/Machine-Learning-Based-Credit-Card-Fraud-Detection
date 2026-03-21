# 💳 Credit Card Fraud Detection System

A Beginner-Friendly Machine Learning Web Application: **Python + Flask + Scikit-learn + MongoDB**

---

## 📌 What This Project Teaches You

- 🤖 Machine Learning Model – Detects fraudulent credit card transactions  
- 🌐 Flask Backend Server – Handles requests and connects the model with the web interface  
- 🗄️ MongoDB Database – Stores transaction data and prediction results  
- 🎨 Frontend – Built using HTML + CSS for user interaction  

---

## 🔄 Data Flow Example — Fraud Prediction

User enters transaction feature values in the web form  
HTML form sends HTTP POST request → http://localhost:5000/predict  
Flask backend receives the request and extracts the transaction features  
Flask loads the trained machine learning model  
The ML model analyzes the transaction data  
The model predicts whether the transaction is:  
Fraudulent 🚨 or Normal Transaction ✅  
Flask sends the prediction result back to the web page  
The transaction data and prediction result are saved in MongoDB  

---

## 🗂️ Project Structure
```
credit-card-fraud-detection/
│
├── model/
│   └── fraud_model.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── train_model.py
├── app.py
├── creditcard.csv
└── requirements.txt
```
---

## 🚀 How to Run — Step by Step

### STEP 1: Install Required Libraries

pip install -r requirements.txt

---

### STEP 2: Train the Machine Learning Model

python train_model.py

This will create:
model/fraud_model.pkl

---

### STEP 3: Start MongoDB Database

net start MongoDB

---

### STEP 4: Run the Flask Application

python app.py

You should see:
Running on http://127.0.0.1:5000

---

### STEP 5: Open the Web Application

http://127.0.0.1:5000

Enter transaction values and click Predict.

---

## ✅ Test That Everything Works

Enter transaction values  
Click Predict  
You should see:
Fraud Transaction 🚨  
or  
Normal Transaction ✅  

Data will also be stored in MongoDB  

---

## 🔍 Understanding the Key Concepts

### What is Fraud Detection?
Fraud detection identifies unauthorized or suspicious financial transactions using machine learning.

### What is a Machine Learning Model?
It learns patterns from past data and predicts whether a transaction is fraud or normal.

### What is Flask?
Flask is a Python web framework used to connect frontend and machine learning model.

### What is MongoDB?
MongoDB is a NoSQL database used to store transaction data and prediction results.

---

## ❓ Common Problems & Solutions

Model file not found → python train_model.py  

MongoDB not running → net start MongoDB  

Module not found → pip install -r requirements.txt  

---

## 📚 What to Learn Next

- Add prediction probability score  
- Create transaction history dashboard  
- Improve UI using Bootstrap or React  
- Deploy using Render / AWS / Heroku  
- Add authentication system  

---

## 👨‍💻 Author

Mamatha Takur
