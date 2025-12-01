@echo off
echo 🌊 River Flood Prediction System - Windows Launcher
echo ================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo    Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo ✓ Python found

REM Check if we're in the right directory
if not exist "backend" (
    echo ❌ Error: Backend directory not found
    echo    Please run this script from the project root directory
    pause
    exit /b 1
)

if not exist "frontend" (
    echo ❌ Error: Frontend directory not found
    echo    Please run this script from the project root directory
    pause
    exit /b 1
)

echo ✓ Project structure found

REM Start the complete system
echo.
echo 🚀 Starting the complete River Flood Prediction System...
echo    This will start both the backend API and frontend web interface
echo.
echo    Backend API: http://localhost:8001
echo    Frontend: http://localhost:8080
echo    API Documentation: http://localhost:8001/docs
echo.
echo    Press Ctrl+C to stop all services
echo.

python start_full_system.py

echo.
echo 👋 System stopped. Goodbye!
pause
