@echo off
echo Starting Code Helper AI...
echo.
echo Please wait while the application starts...
echo.
cd /d "%~dp0"
echo Starting Flask server...
echo.
echo IMPORTANT: Once the server is running, open your web browser and go to:
echo http://127.0.0.1:5000
echo.
echo You can also run open_browser.bat to open the browser automatically.
echo.
python app.py
pause