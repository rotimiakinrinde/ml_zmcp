# Models Folder

## ⚠️ IMPORTANT: Put Your Model Files Here

This folder should contain 3 files from your Jupyter notebook:

1. **random_forest_attrition.pkl** (your trained model)
2. **model_metadata.json** (model information)
3. **feature_names.json** (list of features)

---

## 📂 Where to Copy From

Your notebook created these files at:
```
C:\Users\akinr\Desktop\10Analytics\Python\Machine Learning\models\
```

---

## 💾 How to Copy Files

### Windows PowerShell:
```powershell
# From the parent directory
Copy-Item ..\models\* .\models\ -Force
```

### Or manually:
1. Open File Explorer
2. Navigate to your notebook's `models` folder
3. Copy all 3 files
4. Paste them into this folder

---

## ✅ Verification

After copying, this folder should contain:

```
models/
├── random_forest_attrition.pkl  (37.8 MB)
├── model_metadata.json          (< 1 KB)
└── feature_names.json           (< 1 KB)
```

Check with:
```powershell
ls
```

---

## 🚨 Without These Files

The Docker container **will not start** without these model files.

Make sure all 3 files are present before running:
```powershell
.\deploy.ps1
```

---

**Status**: ❌ Files Missing - Copy your model files here first!
