@echo off
echo.
echo ========================================
echo Student Performance Prediction System
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo Python found!
echo.

REM Navigate to backend
cd backend

REM Check if requirements are installed
echo Checking dependencies...
pip list | find "Flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo Dependencies already installed!
)

echo.
echo ========================================
echo Starting Flask Backend Server...
echo ========================================
echo.
echo Server will start on: http://127.0.0.1:5000
echo.
echo To access the application:
echo 1. Open frontend/index.html in your browser
echo 2. Or run: python -m http.server 8000 (in frontend directory)
echo 3. Then visit: http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
