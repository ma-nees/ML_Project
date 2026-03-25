# 🎓 Student Performance Prediction System

A machine learning-powered web application that predicts student academic performance based on various factors. Built with Flask backend, scikit-learn models, and a modern interactive frontend.

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green)
![License](https://img.shields.io/badge/License-MIT-blue)

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Machine Learning Models](#machine-learning-models)
- [Dataset](#dataset)
- [Architecture](#architecture)
- [Technologies](#technologies)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

✅ **4 Machine Learning Models**
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Logistic Regression

✅ **Real-time Predictions**
- Instant student performance prediction (Pass/Fail)
- Feature scaling and preprocessing

✅ **Interactive Dashboard**
- Modern glassmorphism UI design
- Model accuracy comparison visualization
- Real-time prediction results

✅ **RESTful API**
- CORS-enabled endpoints
- JSON request/response format
- Easy integration with other applications

✅ **Easy Deployment**
- Pre-configured Flask server
- Helper scripts for quick setup
- No additional configuration needed

## 📁 Project Structure

```
student-performance-prediction/
│
├── backend/
│   ├── app.py                      # Flask API server
│   ├── model_training.py           # ML model training pipeline
│   ├── requirements.txt            # Python dependencies
│   ├── models/
│   │   ├── best_model.pkl          # Trained ML model
│   │   ├── scaler.pkl              # Feature scaler
│   │   ├── model_info.pkl          # Model comparison data
│   │   ├── columns.json            # Feature names
│   │   └── accuracy.json           # Model accuracy metrics
│   └── data/
│       └── student-por.csv         # Training dataset
│
├── frontend/
│   ├── index.html                  # Web interface
│   ├── style.css                   # Modern styling
│   └── script.js                   # Frontend logic & API calls
│
├── run_backend.bat/sh              # Quick start scripts
├── train_model.bat/sh              # Model training scripts
├── README.md                       # Documentation
└── QUICKSTART.md                   # Quick start guide
```

## 🚀 Installation

### Prerequisites

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (comes with Python)
- **Git** - Version control
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Step 1: Clone the Repository

```bash
git clone https://github.com/ma-nees/ML_Project.git
cd ml-student-dashboard
```

### Step 2: Set Up Backend

```bash
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Start Backend Server

```bash
python app.py
```

You should see:
```
============================================================
Starting Flask Server...
============================================================
✅ Model loaded successfully
✅ Scaler loaded successfully
✅ Model info loaded successfully
```

### Step 4: Open Frontend

Navigate to `frontend/index.html` in your web browser or serve it locally:

```bash
cd frontend
python -m http.server 8000
```

Then visit: `http://localhost:8000`

## 💻 Quick Start

### Windows Users

```bash
# Simply run:
run_backend.bat
```

Then open `frontend/index.html` in your browser.

### Linux/Mac Users

```bash
# Make scripts executable
chmod +x run_backend.sh

# Run backend
./run_backend.sh
```

Then open `frontend/index.html` in your browser.

## 📖 Usage

### Making a Prediction

1. **Start the backend server** (see Installation steps above)
2. **Open the frontend** in your browser
3. **Fill in student details:**
   - Age: Student's age in years
   - Study Time: Weekly study hours (1-10)
   - Failures: Number of past class failures (0+)
   - Absences: Number of school absences (0+)
   - G1: First period grade (0-20)
   - G2: Second period grade (0-20)

4. **Click "🚀 Predict"**
5. **View the result:** ✅ PASS or ❌ FAIL
6. **Compare models:** See accuracy metrics for all trained models

### Retraining Models

To retrain the ML models with new data:

```bash
cd backend
python model_training.py
```

Or use the helper script:
- Windows: `train_model.bat`
- Linux/Mac: `./train_model.sh`

## 🔌 API Endpoints

### Base URL
```
http://127.0.0.1:5000
```

### POST `/predict`
Predicts student pass/fail status.

**Request:**
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 18,
    "studytime": 2,
    "failures": 0,
    "absences": 5,
    "G1": 12,
    "G2": 14
  }'
```

**Response:**
```json
{
  "prediction": "PASS",
  "status": "success"
}
```

### GET `/model-info`
Returns model accuracies and comparison data.

**Request:**
```bash
curl http://127.0.0.1:5000/model-info
```

**Response:**
```json
{
  "K-Nearest Neighbors (KNN)": 0.8234,
  "Decision Tree": 0.7956,
  "Random Forest": 0.8562,
  "Logistic Regression": 0.8234
}
```

### GET `/health`
Checks server health status.

**Request:**
```bash
curl http://127.0.0.1:5000/health
```

**Response:**
```json
{
  "status": "healthy",
  "models_loaded": 4
}
```

## 🤖 Machine Learning Models

The system trains and evaluates **4 different classification models**:

### 1. **K-Nearest Neighbors (KNN)**
- **Type:** Distance-based classifier
- **Pros:** Simple, intuitive, no training phase
- **Cons:** Slow on large datasets, sensitive to feature scaling

### 2. **Decision Tree**
- **Type:** Rule-based tree structure
- **Pros:** Interpretable, handles non-linear relationships
- **Cons:** Prone to overfitting, can be biased

### 3. **Random Forest** ⭐ (Usually Best Performer)
- **Type:** Ensemble of decision trees
- **Pros:** High accuracy, robust, handles non-linearity well
- **Cons:** Requires more computational resources

### 4. **Logistic Regression**
- **Type:** Linear probabilistic classifier
- **Pros:** Fast, interpretable, good baseline
- **Cons:** Assumes linear relationships

**Best Model Selection:**
The model with the highest test accuracy is automatically selected for production predictions.

## 📊 Dataset

**File:** `backend/data/student-por.csv`

**Overview:**
- **Total Records:** 649 students
- **Features:** 30+ attributes
- **Target:** G3 (Final Grade)

**Key Features Used:**
- `age` - Student age (15-22)
- `studytime` - Weekly study hours (1-10)
- `failures` - Past class failures (0-4)
- `absences` - School absences (0-93)
- `G1` - First period grade (0-20)
- `G2` - Second period grade (0-20)
- `G3` - Final grade (0-20) [TARGET]

**Target Variable:**
- **Pass:** G3 ≥ 10
- **Fail:** G3 < 10

**Data Characteristics:**
- Portuguese secondary school students
- Binary classification problem
- Balanced dataset
- No missing values after preprocessing

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│          Frontend (Client)              │
│  - index.html (Web Interface)           │
│  - script.js (API calls, logic)         │
│  - style.css (Modern UI)                │
└────────────────┬────────────────────────┘
                 │
                 │ HTTP/JSON
                 │
┌────────────────▼────────────────────────┐
│       Flask Backend (Server)            │
│  - app.py (REST API endpoints)          │
│  - /predict (POST)                      │
│  - /model-info (GET)                    │
│  - /health (GET)                        │
└────────────────┬────────────────────────┘
                 │
         ┌───────┴────────┐
         │                │
    ┌────▼──────┐  ┌─────▼──────┐
    │   Model   │  │   Scaler   │
    │ (pkl)     │  │   (pkl)    │
    └───────────┘  └────────────┘
         │
    ┌────▼──────────┐
    │  Trained ML   │
    │  Models       │
    │  (4 types)    │
    └───────────────┘
```

## 🛠️ Technologies

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| Flask | 2.3.0 | Web framework |
| scikit-learn | 1.2.0 | Machine learning |
| pandas | 2.0.0 | Data manipulation |
| numpy | 1.24.0 | Numerical computing |
| joblib | 1.2.0 | Model serialization |
| Flask-CORS | 4.0.0 | Cross-origin requests |

### Frontend
| Technology | Purpose |
|------------|---------|
| HTML5 | Structure |
| CSS3 | Modern styling (glassmorphism) |
| JavaScript (ES6+) | Interactivity |
| Chart.js | Data visualization |

### DevOps
| Tool | Purpose |
|------|---------|
| Git | Version control |
| GitHub | Repository hosting |
| Python venv | Environment management |

## 🔧 Troubleshooting

### Issue: "Python not found"
**Solution:**
- Install Python from [python.org](https://www.python.org/downloads/)
- Ensure Python is added to your system PATH
- Verify: `python --version`

### Issue: "Port 5000 already in use"
**Solution:**
```bash
# Find and kill process using port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac:
lsof -ti:5000 | xargs kill -9
```

### Issue: "Module not found" (numpy, pandas, etc.)
**Solution:**
```bash
# Ensure virtual environment is activated
pip install -r requirements.txt
```

### Issue: "Backend connection failed"
**Solution:**
- Verify Flask server is running
- Check if server is on `http://127.0.0.1:5000`
- Check browser console for CORS errors
- Ensure CORS is enabled in `app.py`

### Issue: "Models not found"
**Solution:**
```bash
cd backend
python model_training.py
# Wait for training to complete
python app.py
```

### Issue: "CORS Error in browser"
**Solution:**
- Ensure Flask server is running with CORS enabled
- Check browser console for specific error
- Try opening from `http://localhost:8000` instead of `file://`

## 🚀 Performance Metrics

Models are evaluated on a test set (20% of data) using:

- **Accuracy:** Correct predictions / Total predictions
- **Precision:** True positives / (True positives + False positives)
- **Recall:** True positives / (True positives + False negatives)
- **F1-Score:** Harmonic mean of precision and recall

## 📈 Expected Results

Typical model accuracies on test set:
- Random Forest: 85-90%
- KNN: 80-85%
- Logistic Regression: 80-85%
- Decision Tree: 75-80%

Results may vary based on data split and random seed.

## 🔐 Security Considerations

⚠️ **Note:** This is an educational project. For production use:
- Add authentication and authorization
- Use HTTPS instead of HTTP
- Validate and sanitize all inputs
- Add rate limiting
- Use environment variables for sensitive data
- Implement logging and monitoring

## 📝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Known Issues

- Model training can take 30-60 seconds
- Large CSV files may slow down training
- Frontend requires modern browser with ES6 support
- Predictions work best with normalized input values

## 🔮 Future Enhancements

- [ ] Add feature importance visualization
- [ ] Implement cross-validation
- [ ] Add batch prediction support
- [ ] Create admin dashboard
- [ ] Add model monitoring and drift detection
- [ ] Implement A/B testing for models
- [ ] Deploy to cloud (Azure, AWS)
- [ ] Add mobile app support
- [ ] Integrate with learning management systems
- [ ] Add explainable AI (SHAP/LIME)

## 📚 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [scikit-learn Guide](https://scikit-learn.org/)
- [pandas Tutorial](https://pandas.pydata.org/docs/)
- [Machine Learning Basics](https://www.coursera.org/learn/machine-learning)

## 📞 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/ma-nees/ML_Project/issues)
- Check [QUICKSTART.md](QUICKSTART.md) for quick reference
- Review [Troubleshooting](#troubleshooting) section

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💼 Author

**Manees**
- GitHub: [@ma-nees](https://github.com/ma-nees)
- Project: [ML_Project](https://github.com/ma-nees/ML_Project)

## 🙏 Acknowledgments

- Student-Por dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
- Icons from [Font Awesome](https://fontawesome.com/)
- Chart visualization by [Chart.js](https://www.chartjs.org/)

---

**Happy Predicting!** 🎓✨

*Last Updated: March 2026*
*Version: 1.0.0*
