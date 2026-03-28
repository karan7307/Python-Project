from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from model import load_trained_model
from data_processor import preprocess_data
import os

app = Flask(__name__)

# Global model instance
model = load_trained_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        data = request.json
        # Extract features from request
        features = np.array([[
            data['study_hours'],
            data['stress_level'],
            data['sleep_hours'],
            data['extracurricular_activities']
        ]])
        
        # Scaling (In a real app, you'd use a saved scaler)
        prediction = model.predict(features)[0][0]
        
        return jsonify({"burnout_score": float(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
