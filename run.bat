@echo off
title PIXSEE Automation Runner

:: -----------------------------
:: Step 1 - User input
:: -----------------------------
set /p device_name=Enter your device name (adb devices ID): 
set /p account=Enter your account: 
set /p password=Enter your password: 

:: -----------------------------
:: Step 2 - Install requirements (first run only)
:: -----------------------------
if not exist venv (
    echo First run detected, installing requirements...
    pip install -r requirements.txt
)

:: -----------------------------
:: Step 3 - Set environment variables
:: -----------------------------
set DEVICE_NAME=%device_name%
set ACCOUNT=%account%
set PASSWORD=%password%

:: -----------------------------
:: Step 4 - Start Appium server
:: -----------------------------
echo Starting Appium server...
start cmd /k "appium --use-plugins=inspector --allow-cors"
timeout /t 5 >nul

:: -----------------------------
:: Step 5 - Choose which test to run
:: -----------------------------
echo.
set /p choice=Run (1) Subscription test or (2) Unsubscription test? Enter 1 or 2: 

if "%choice%"=="1" (
    python subscription_main.py
) else (
    python unsubscription_main.py
)

pause
