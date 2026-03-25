#!/bin/bash

echo ""
echo "========================================"
echo "Training Student Performance Model"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "Python found!"
echo ""

# Navigate to backend
cd backend

# Install dependencies if needed
echo "Checking dependencies..."
python3 -m pip list | grep scikit-learn > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    python3 -m pip install -r requirements.txt
fi

echo ""
echo "Training models..."
echo ""

python3 model_training.py

if [ $? -ne 0 ]; then
    echo "Error: Model training failed"
    exit 1
fi

echo ""
echo "Model training completed!"
