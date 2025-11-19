# 🚀 SETUP INSTRUCTIONS - START HERE

## What You Have

A complete Docker deployment package for your Employee Attrition Prediction model.

Your model: **82.29% accuracy** Random Forest Classifier ✓

---

## ⚡ Quick Setup (5 Minutes)

### Step 1: Copy Model Files (2 minutes)

You need to copy 3 files from your notebook's `models` folder:

**From:**
```
C:\Users\akinr\Desktop\10Analytics\Python\Machine Learning\models\
├── random_forest_attrition.pkl
├── model_metadata.json
└── feature_names.json
```

**To:**
```
docker_deployment_package\models\
├── random_forest_attrition.pkl   ← Copy here
├── model_metadata.json           ← Copy here
└── feature_names.json            ← Copy here
```

**PowerShell command:**
```powershell
# If both folders are in the same directory
Copy-Item ..\models\* .\models\ -Force

# Or specify full paths
Copy-Item "C:\Users\akinr\Desktop\10Analytics\Python\Machine Learning\models\*" ".\models\" -Force
```

### Step 2: Verify Files (30 seconds)

```powershell
# Check that all 3 files are there
ls models\
```

You should see:
- ✓ random_forest_attrition.pkl (37.8 MB)
- ✓ model_metadata.json (< 1 KB)
- ✓ feature_names.json (< 1 KB)

### Step 3: Deploy (2 minutes)

```powershell
# Option A: Use the automated script
.\deploy.ps1

# Option B: Manual deployment
docker-compose build
docker-compose up -d
```

### Step 4: Test (30 seconds)

```powershell
# Quick health check
curl http://localhost:5000/health

# Or run full tests
python tests\test_api.py
```

---

## ✅ Success!

If you see:
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

**Congratulations! Your API is live at http://localhost:5000** 🎉

---

## 📖 What's Next?

1. **Make a prediction** - See README.md for examples
2. **Test with your data** - Use the `/predict` endpoint
3. **Read full documentation** - See README.md

---

## 🆘 Having Issues?

### Issue: Can't find model files
```powershell
# Check where your models are
Get-ChildItem -Path "C:\Users\akinr\Desktop\10Analytics\Python\Machine Learning" -Recurse -Filter "*.pkl"
```

### Issue: Docker not installed
1. Download from: https://www.docker.com/products/docker-desktop
2. Install and restart
3. Try again

### Issue: Port 5000 in use
```powershell
# Stop any existing container
docker-compose down

# Or use different port (edit docker-compose.yml)
```

---

## 📁 Package Contents

```
docker_deployment_package/
├── 📄 SETUP_INSTRUCTIONS.md  ← You are here
├── 📄 README.md              ← Full documentation
├── 📄 Dockerfile             ← Container config
├── 📄 docker-compose.yml     ← Deployment config
├── 📄 requirements.txt       ← Python packages
├── 🔧 deploy.ps1            ← Windows deployment script
├── 📁 app/
│   └── app.py               ← Flask API
├── 📁 models/               ← PUT YOUR FILES HERE!
└── 📁 tests/
    └── test_api.py          ← API tests
```

---

## 🎯 Checklist

- [ ] Downloaded this package
- [ ] Extracted to your working directory
- [ ] Copied 3 model files to `models/` folder
- [ ] Docker Desktop installed and running
- [ ] Ran `.\deploy.ps1` or `docker-compose up -d`
- [ ] API health check passed
- [ ] Made a test prediction

---

**Time Required**: 5 minutes  
**Difficulty**: Easy  
**Prerequisites**: Docker Desktop

**Need help?** See README.md for detailed documentation.
