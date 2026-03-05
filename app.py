from flask import Flask, render_template, request
import joblib
import numpy as np
from pymongo import MongoClient

app = Flask(__name__)

# Load trained model
model = joblib.load("model/fraud_model.pkl")
# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["fraudDB"]
collection = db["transactions"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array([features])

    prediction = model.predict(final_features)

  # Save data in MongoDB
    collection.insert_one({
        "features": features,
        "prediction": int(prediction[0])
    })
    
    if prediction[0] == 1:
        result = "Fraud Transaction 🚨"
    else:
        result = "Normal Transaction ✅"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)