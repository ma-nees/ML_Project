@echo off
echo.
echo ========================================
echo Training Student Performance Model
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

REM Install dependencies if needed
echo Checking dependencies...
pip list | find "scikit-learn" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo.
echo Training models...
echo.

python model_training.py

if %errorlevel% neq 0 (
    echo Error: Model training failed
    pause
    exit /b 1
)

echo.
echo Model training completed!
pause
