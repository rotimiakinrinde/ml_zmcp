# Employee Attrition Prediction API - Docker Deployment

Deploy your Random Forest model (82.29% accuracy) as a production-ready API.

## 📋 What's Included

- ✅ Flask API with 4 endpoints
- ✅ Dockerfile for containerization
- ✅ docker-compose.yml for easy deployment
- ✅ Automated test suite
- ✅ Windows PowerShell deployment script
- ✅ Complete documentation

## 🚀 Quick Start (3 Steps)

### Step 1: Copy Your Model Files

Copy your model files from your notebook's `models` folder to this package's `models` folder:

```powershell
# Windows PowerShell
Copy-Item ..\models\* .\models\ -Force
```

You should have these 3 files:
- `models/random_forest_attrition.pkl`
- `models/model_metadata.json`
- `models/feature_names.json`

### Step 2: Deploy

```powershell
# Run the deployment script
.\deploy.ps1
```

Or manually:
```powershell
docker-compose build
docker-compose up -d
```

### Step 3: Test

```powershell
# Run tests
python tests\test_api.py

# Or test manually
curl http://localhost:5000/health
```

That's it! Your API is now running at `http://localhost:5000`

---

## 📁 Folder Structure

```
docker_deployment_package/
├── app/
│   └── app.py              # Flask API
├── models/                 # PUT YOUR MODEL FILES HERE
│   ├── random_forest_attrition.pkl   ← Copy from notebook
│   ├── model_metadata.json           ← Copy from notebook
│   └── feature_names.json            ← Copy from notebook
├── tests/
│   └── test_api.py         # API tests
├── Dockerfile              # Container definition
├── docker-compose.yml      # Docker orchestration
├── requirements.txt        # Python dependencies
├── deploy.ps1             # Windows deployment script
└── README.md              # This file
```

---

## 🔌 API Endpoints

### 1. Health Check
```http
GET http://localhost:5000/health
```

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "metadata_loaded": true,
  "feature_count": 9,
  "timestamp": "2024-11-19T12:34:56"
}
```

### 2. Model Information
```http
GET http://localhost:5000/model/info
```

**Response:**
```json
{
  "model_type": "RandomForestClassifier",
  "training_date": "2024-11-19T18:29:00",
  "test_accuracy": 0.8229,
  "n_features": 9,
  "feature_names": ["Age", "Gender", "Department", ...],
  "class_names": ["No Attrition", "Attrition"]
}
```

### 3. Single Prediction
```http
POST http://localhost:5000/predict
Content-Type: application/json

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
}
```

**Response:**
```json
{
  "prediction": 1,
  "prediction_label": "Attrition",
  "probability": {
    "no_attrition": 0.35,
    "attrition": 0.65
  },
  "confidence": 0.65,
  "timestamp": "2024-11-19T12:34:56"
}
```

### 4. Batch Prediction
```http
POST http://localhost:5000/predict/batch
Content-Type: application/json

{
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
```

---

## 💻 Usage Examples

### Python Example

```python
import requests

# Single prediction
employee = {
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

response = requests.post(
    'http://localhost:5000/predict',
    json=employee
)

result = response.json()
print(f"Prediction: {result['prediction_label']}")
print(f"Confidence: {result['confidence']:.2%}")
```

### PowerShell Example

```powershell
# Test the API
$employee = @{
    Age = 35
    Gender = "Male"
    Department = "IT"
    MonthlyIncome = 5500
    YearsAtCompany = 3
    OverTime = "Yes"
    JobSatisfaction = 2
    WorkLifeBalance = 2
    TrainingTimesLastYear = 1
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/predict" -Method POST -Body $employee -ContentType "application/json"
```

---

## 🛠️ Common Commands

### Windows PowerShell

```powershell
# Start the API
docker-compose up -d

# Stop the API
docker-compose down

# View logs
docker-compose logs -f

# Restart the API
docker-compose restart

# Check container status
docker-compose ps

# Rebuild after changes
docker-compose up -d --build
```

---

## 🐛 Troubleshooting

### Problem: "Cannot find model files"

**Solution:**
```powershell
# Check if files exist
ls models\

# If missing, copy from your notebook's models folder
Copy-Item ..\models\* .\models\ -Force
```

### Problem: "Port 5000 already in use"

**Solution 1: Stop existing service**
```powershell
# Find what's using port 5000
Get-NetTCPConnection -LocalPort 5000

# Stop Docker container
docker-compose down
```

**Solution 2: Use different port**
Edit `docker-compose.yml`:
```yaml
ports:
  - "8080:5000"  # Use port 8080 instead
```

### Problem: "Docker is not running"

**Solution:**
1. Open Docker Desktop
2. Wait for Docker to start
3. Try again

### Problem: Container keeps restarting

**Check logs:**
```powershell
docker-compose logs
```

Common causes:
- Model files missing
- Python package error
- Port conflict

---

## 📊 Model Performance

Your deployed model:
- **Accuracy**: 82.29%
- **Model Type**: Random Forest Classifier
- **Training Date**: Check `/model/info` endpoint
- **Features**: 9 input features

---

## ✅ Verification Checklist

Before deploying:
- [ ] Docker Desktop installed and running
- [ ] Model files copied to `models/` folder
- [ ] All 3 model files present (`.pkl`, 2 `.json` files)

After deploying:
- [ ] Container running (`docker-compose ps`)
- [ ] Health check passes (`curl http://localhost:5000/health`)
- [ ] Can make predictions
- [ ] Tests pass (`python tests\test_api.py`)

---

## 🚀 Next Steps

1. **Test with your data** - Validate predictions
2. **Deploy to cloud** - AWS, Azure, or GCP
3. **Add authentication** - Secure your API
4. **Monitor performance** - Track predictions
5. **Set up CI/CD** - Automated deployments

---

## 📞 Support

### Common Issues
- Model not loading → Check file paths
- API not responding → Check Docker logs
- Wrong predictions → Verify input features

### Check Status
```powershell
# API health
curl http://localhost:5000/health

# Container status
docker-compose ps

# View logs
docker-compose logs --tail=50
```

---

## 🎯 Quick Reference

| Command | Purpose |
|---------|---------|
| `.\deploy.ps1` | Deploy everything |
| `docker-compose up -d` | Start API |
| `docker-compose down` | Stop API |
| `docker-compose logs -f` | View logs |
| `python tests\test_api.py` | Run tests |
| `curl http://localhost:5000/health` | Check health |

---

**Created**: November 2024  
**Version**: 1.0  
**Model Accuracy**: 82.29%  
**Status**: Production Ready ✅
