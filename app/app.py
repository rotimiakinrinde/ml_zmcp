"""
Flask API for Employee Attrition Prediction
"""

from flask import Flask, request, jsonify
import joblib
import json
import pandas as pd
import numpy as np
from datetime import datetime
import os

app = Flask(__name__)

# Load model and metadata at startup
MODEL_PATH = 'models/random_forest_attrition.pkl'
METADATA_PATH = 'models/model_metadata.json'
FEATURE_NAMES_PATH = 'models/feature_names.json'

model = None
metadata = None
feature_names = None


def load_model():
    """Load the trained model and metadata"""
    global model, metadata, feature_names
    
    try:
        print("Loading model...")
        model = joblib.load(MODEL_PATH)
        
        print("Loading metadata...")
        with open(METADATA_PATH, 'r') as f:
            metadata = json.load(f)
        
        print("Loading feature names...")
        with open(FEATURE_NAMES_PATH, 'r') as f:
            feature_names = json.load(f)['features']
        
        print(f"✓ Model loaded successfully!")
        print(f"  Model type: {metadata.get('model_type', 'Unknown')}")
        print(f"  Test accuracy: {metadata.get('test_accuracy', 'Unknown')}")
        print(f"  Number of features: {len(feature_names)}")
        
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        raise


# Load model when app starts
load_model()


@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Employee Attrition Prediction API',
        'version': '1.0.0',
        'model_type': metadata.get('model_type', 'Unknown'),
        'model_accuracy': metadata.get('test_accuracy', 'Unknown')
    })


@app.route('/health', methods=['GET'])
def health():
    """Detailed health check"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'metadata_loaded': metadata is not None,
        'feature_count': len(feature_names) if feature_names else 0,
        'timestamp': datetime.now().isoformat()
    })


@app.route('/model/info', methods=['GET'])
def model_info():
    """Get model information"""
    if metadata is None:
        return jsonify({'error': 'Model metadata not loaded'}), 500
    
    return jsonify({
        'model_type': metadata.get('model_type'),
        'training_date': metadata.get('training_date'),
        'test_accuracy': metadata.get('test_accuracy'),
        'n_features': len(feature_names),
        'feature_names': feature_names,
        'class_names': metadata.get('class_names', ['No Attrition', 'Attrition'])
    })


@app.route('/predict', methods=['POST'])
def predict():
    """
    Make a prediction for a single employee
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Convert to DataFrame
        df = pd.DataFrame([data])
        
        # Check for missing features
        missing_features = set(feature_names) - set(df.columns)
        if missing_features:
            return jsonify({
                'error': 'Missing required features',
                'missing_features': list(missing_features),
                'required_features': feature_names
            }), 400
        
        # Reorder columns to match training
        df = df[feature_names]
        
        # Make prediction
        prediction = model.predict(df)[0]
        prediction_proba = model.predict_proba(df)[0]
        
        # Prepare response
        result = {
            'prediction': int(prediction),
            'prediction_label': metadata.get('class_names', ['No Attrition', 'Attrition'])[prediction],
            'probability': {
                'no_attrition': float(prediction_proba[0]),
                'attrition': float(prediction_proba[1])
            },
            'confidence': float(max(prediction_proba)),
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'error': 'Prediction failed',
            'message': str(e)
        }), 500


@app.route('/predict/batch', methods=['POST'])
def predict_batch():
    """
    Make predictions for multiple employees
    """
    try:
        data = request.get_json()
        
        if not data or 'employees' not in data:
            return jsonify({'error': 'No employee data provided. Expected format: {"employees": [...]}'}), 400
        
        employees = data['employees']
        
        if not isinstance(employees, list):
            return jsonify({'error': 'employees must be a list'}), 400
        
        # Convert to DataFrame
        df = pd.DataFrame(employees)
        
        # Check for missing features
        missing_features = set(feature_names) - set(df.columns)
        if missing_features:
            return jsonify({
                'error': 'Missing required features',
                'missing_features': list(missing_features),
                'required_features': feature_names
            }), 400
        
        # Reorder columns
        df = df[feature_names]
        
        # Make predictions
        predictions = model.predict(df)
        predictions_proba = model.predict_proba(df)
        
        # Prepare results
        results = []
        class_names = metadata.get('class_names', ['No Attrition', 'Attrition'])
        for i, (pred, proba) in enumerate(zip(predictions, predictions_proba)):
            results.append({
                'employee_index': i,
                'prediction': int(pred),
                'prediction_label': class_names[pred],
                'probability': {
                    'no_attrition': float(proba[0]),
                    'attrition': float(proba[1])
                },
                'confidence': float(max(proba))
            })
        
        # Summary statistics
        summary = {
            'total_employees': len(results),
            'predicted_attrition': int(sum(predictions)),
            'predicted_retention': int(len(predictions) - sum(predictions)),
            'attrition_rate': float(sum(predictions) / len(predictions))
        }
        
        return jsonify({
            'predictions': results,
            'summary': summary,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Batch prediction failed',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
