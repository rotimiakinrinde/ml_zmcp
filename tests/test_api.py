"""
Test script for the Attrition Prediction API
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"


def test_health():
    """Test health check"""
    print("\n" + "="*60)
    print("Testing Health Check...")
    print("="*60)
    
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_model_info():
    """Test model info"""
    print("\n" + "="*60)
    print("Testing Model Info...")
    print("="*60)
    
    response = requests.get(f"{BASE_URL}/model/info")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_single_prediction():
    """Test single prediction"""
    print("\n" + "="*60)
    print("Testing Single Prediction...")
    print("="*60)
    
    employee_data = {
        "Age": 35,
        "Gender": "Male",
        "Department": "IT",
        "MonthlyIncome": 5500,
        "YearsAtCompany": 3,
        "OverTime": "Yes",
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "TrainingTimesLastYear": 1
    }
    
    print("Input Data:")
    print(json.dumps(employee_data, indent=2))
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=employee_data,
        headers={'Content-Type': 'application/json'}
    )
    
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_batch_prediction():
    """Test batch prediction"""
    print("\n" + "="*60)
    print("Testing Batch Prediction...")
    print("="*60)
    
    batch_data = {
        "employees": [
            {
                "Age": 35,
                "Gender": "Male",
                "Department": "IT",
                "MonthlyIncome": 5500,
                "YearsAtCompany": 3,
                "OverTime": "Yes",
                "JobSatisfaction": 2,
                "WorkLifeBalance": 2,
                "TrainingTimesLastYear": 1
            },
            {
                "Age": 42,
                "Gender": "Female",
                "Department": "HR",
                "MonthlyIncome": 7500,
                "YearsAtCompany": 8,
                "OverTime": "No",
                "JobSatisfaction": 4,
                "WorkLifeBalance": 4,
                "TrainingTimesLastYear": 3
            }
        ]
    }
    
    response = requests.post(
        f"{BASE_URL}/predict/batch",
        json=batch_data,
        headers={'Content-Type': 'application/json'}
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("API Testing Suite")
    print("="*60)
    
    # Wait for API
    print("\nWaiting for API to be ready...")
    max_retries = 10
    for i in range(max_retries):
        try:
            response = requests.get(f"{BASE_URL}/health", timeout=2)
            if response.status_code == 200:
                print("✓ API is ready!")
                break
        except:
            if i < max_retries - 1:
                print(f"  Attempt {i+1}/{max_retries} - waiting...")
                time.sleep(2)
            else:
                print("✗ API is not responding")
                return
    
    # Run tests
    results = {
        'Health Check': test_health(),
        'Model Info': test_model_info(),
        'Single Prediction': test_single_prediction(),
        'Batch Prediction': test_batch_prediction()
    }
    
    # Summary
    print("\n" + "="*60)
    print("Test Results Summary")
    print("="*60)
    for test_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    total = len(results)
    passed = sum(results.values())
    print(f"\nTotal: {passed}/{total} tests passed")


if __name__ == "__main__":
    run_all_tests()
