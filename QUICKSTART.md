# Quick Start Guide - Student Performance Prediction System

## 🚀 5 Minute Setup

### For Windows Users

1. **Clone/Extract the project** and navigate to the directory

2. **Run the startup script:**
   ```
   run_backend.bat
   ```
   This will:
   - Check for Python installation
   - Install dependencies
   - Start the Flask server

3. **Open in browser:**
   - Navigate to `frontend/index.html` and open with your browser

4. **Make a prediction!**
   - Fill in student details
   - Click "🚀 Predict"

### For Mac/Linux Users

1. **Clone/Extract the project** and navigate to the directory

2. **Make scripts executable:**
   ```bash
   chmod +x run_backend.sh train_model.sh
   ```

3. **Run the startup script:**
   ```bash
   ./run_backend.sh
   ```
   This will:
   - Check for Python installation
   - Install dependencies
   - Start the Flask server

4. **Open in browser:**
   - Navigate to `frontend/index.html` and open with your browser

5. **Make a prediction!**
   - Fill in student details
   - Click "🚀 Predict"

## 📋 Manual Setup (If Scripts Don't Work)

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# (Recommended) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

### Frontend Setup

In a **new terminal** (keep backend running):

```bash
cd frontend
python -m http.server 8000
```

Then open: `http://localhost:8000`

## 🔄 Retraining Models

If you want to retrain the ML models with new data:

```bash
# Run the training script
python model_training.py
```

Or use the batch script:
- **Windows:** `train_model.bat`
- **Mac/Linux:** `./train_model.sh`

## 🧪 Testing the API

### Using curl:

```bash
# Test prediction endpoint
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"age":18, "studytime":2, "failures":0, "absences":2, "G1":10, "G2":12}'

# Get model info
curl http://127.0.0.1:5000/model-info
```

### Using Python:

```python
import requests

response = requests.post('http://127.0.0.1:5000/predict', json={
    "age": 18,
    "studytime": 2,
    "failures": 0,
    "absences": 2,
    "G1": 10,
    "G2": 12
})

print(response.json())
```

## 📊 Understanding the Results

The system predicts:
- **✅ PASS** - Student likely to pass (final grade ≥ 10)
- **❌ FAIL** - Student likely to fail (final grade < 10)

The accuracy metrics show how well each model performs on test data.

## ⚠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| "Python not found" | Install Python 3.8+ from python.org |
| "Module not found" | Run `pip install -r requirements.txt` |
| "Port 5000 in use" | Change Flask port or close other app using it |
| "CORS error" | Ensure Flask server is running |
| "Backend connection failed" | Check if `http://127.0.0.1:5000` is accessible |

## 📁 Project Structure

```
├── run_backend.bat/sh         ← Start backend
├── train_model.bat/sh         ← Retrain models
├── README.md                  ← Full documentation
├── backend/
│   ├── app.py                 ← Flask API
│   ├── model_training.py      ← ML pipeline
│   ├── requirements.txt       ← Dependencies
│   ├── model/
│   │   ├── model.pkl          ← Trained model
│   │   ├── scaler.pkl         ← Feature scaler
│   │   ├── accuracy.json      ← Metrics
│   │   └── columns.json       ← Features
│   └── data/
│       └── student-por.csv    ← Training data
└── frontend/
    ├── index.html             ← Web interface
    ├── style.css              ← Styling
    └── script.js              ← Frontend logic
```

## 🎯 Next Steps

1. ✅ Start the backend server
2. ✅ Open the frontend in your browser
3. ✅ Enter sample student data
4. ✅ Click "Predict"
5. ✅ View results and model comparison

## 📞 Need Help?

- Refer to `README.md` for detailed documentation
- Check API endpoints section for API usage
- Review the troubleshooting guide above

---

**Happy Predicting!** 🎓
