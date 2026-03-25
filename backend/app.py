# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

print("="*60)
print("Starting Flask Server...")
print("="*60)

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(script_dir, 'models')

# Load artifacts
try:
    model = joblib.load(os.path.join(models_dir, 'model.pkl'))
    print("✅ Model loaded successfully")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit(1)

try:
    scaler = joblib.load(os.path.join(models_dir, 'scaler.pkl'))
    print("✅ Scaler loaded successfully")
except Exception as e:
    print(f"❌ Error loading scaler: {e}")
    exit(1)

try:
    with open(os.path.join(models_dir, 'columns.json'), 'r') as f:
        feature_columns = json.load(f)
    print(f"✅ Loaded {len(feature_columns)} feature columns")
except Exception as e:
    print(f"❌ Error loading columns: {e}")
    exit(1)

try:
    with open(os.path.join(models_dir, 'model_comparison.json'), 'r') as f:
        model_info = json.load(f)
    print("✅ Model accuracies loaded")
    for name, acc in model_info.items():
        print(f"   {name}: {acc*100:.2f}%")
except Exception as e:
    print(f"⚠️ Could not load model comparison: {e}")
    model_info = {}

# Feature mapping for input
FEATURE_MAPPING = {
    'age': 'age',
    'studytime': 'studytime',
    'failures': 'failures',
    'absences': 'absences',
    'G1': 'G1',
    'G2': 'G2'
}

@app.route('/health', methods=['GET', 'OPTIONS'])
def health():
    if request.method == 'OPTIONS':
        return '', 200
    return jsonify({
        'status': 'healthy',
        'models_loaded': len(model_info),
        'features': len(feature_columns)
    })

@app.route('/model-info', methods=['GET', 'OPTIONS'])
def model_info_endpoint():
    if request.method == 'OPTIONS':
        return '', 200
    return jsonify(model_info)

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.json
        print(f"\n📝 Prediction request received:")
        
        # Create a DataFrame with all features (set to 0 by default)
        input_data = {col: 0 for col in feature_columns}
        
        # Fill in the values from the request
        for user_feature, model_feature in FEATURE_MAPPING.items():
            if user_feature in data:
                input_data[model_feature] = float(data[user_feature])
        
        print(f"   Input features: {input_data}")
        
        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Ensure columns are in the correct order
        input_df = input_df[feature_columns]
        
        # Scale features
        input_scaled = scaler.transform(input_df)
        
        # Predict
        prediction = model.predict(input_scaled)[0]
        result = 'PASS' if prediction == 1 else 'FAIL'
        
        # Get probability if available
        probability = None
        if hasattr(model, 'predict_proba'):
            proba = model.predict_proba(input_scaled)[0]
            probability = float(proba[1]) if prediction == 1 else float(proba[0])
            print(f"   Confidence: {probability*100:.2f}%")
        
        print(f"   Prediction: {result}")
        
        return jsonify({
            'prediction': result,
            'probability': probability,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"❌ Error in prediction: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Student Performance Prediction API',
        'endpoints': {
            '/predict': 'POST - Make predictions',
            '/model-info': 'GET - Get model accuracies',
            '/health': 'GET - Check server health'
        },
        'models_available': list(model_info.keys())
    })

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Server is running!")
    print("   Access the dashboard at: http://127.0.0.1:5000")
    print("   API endpoints:")
    print("   - POST /predict : Make predictions")
    print("   - GET /model-info : Get model accuracies")
    print("   - GET /health : Check server status")
    print("="*60)
    app.run(debug=True, host='0.0.0.0', port=5000)