@echo off
title Calculator
cd /d "%~dp0"

echo ========================================
echo   Calculator Launcher
echo ========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH.
    echo Download Python from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

:: Check if virtual environment exists
if not exist "venv\Scripts\python.exe" (
    echo Setting up virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo ERROR: Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo.
    echo Installing dependencies...
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install dependencies.
        pause
        exit /b 1
    )
    echo.
)

echo Starting Calculator...
echo.
venv\Scripts\python.exe main.py
pause
