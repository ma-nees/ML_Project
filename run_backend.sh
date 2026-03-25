#!/bin/bash

echo "========================================"
echo "Student Performance Prediction System"
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

# Check if requirements are installed
echo "Checking dependencies..."
python3 -m pip list | grep Flask > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    python3 -m pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
else
    echo "Dependencies already installed!"
fi

echo ""
echo "========================================"
echo "Starting Flask Backend Server..."
echo "========================================"
echo ""
echo "Server will start on: http://127.0.0.1:5000"
echo ""
echo "To access the application:"
echo "1. Open frontend/index.html in your browser"
echo "2. Or run: python3 -m http.server 8000 (in frontend directory)"
echo "3. Then visit: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
