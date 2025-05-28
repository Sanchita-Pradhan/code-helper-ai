@echo off
echo Starting Code Helper AI...
echo.
echo Please wait while the application starts...
echo.
cd /d "%~dp0"
start "" http://127.0.0.1:5000
python app.py
pause