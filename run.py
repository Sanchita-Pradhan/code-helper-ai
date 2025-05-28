import os
import sys
import subprocess
import webbrowser
from time import sleep

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required.")
        sys.exit(1)

def check_api_key():
    """Check if the API key is set in the .env file."""
    if not os.path.exists('.env'):
        print("Warning: .env file not found.")
        api_key = input("Please enter your Gemini API key: ")
        with open('.env', 'w') as f:
            f.write(f"GEMINI_API_KEY={api_key}")
        print("API key saved to .env file.")
    else:
        with open('.env', 'r') as f:
            content = f.read()
        if 'GEMINI_API_KEY=' not in content or 'GEMINI_API_KEY=your_api_key_here' in content:
            api_key = input("Please enter your Gemini API key: ")
            with open('.env', 'w') as f:
                f.write(f"GEMINI_API_KEY={api_key}")
            print("API key saved to .env file.")

def install_dependencies():
    """Install required Python packages."""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("Error: Failed to install dependencies.")
        sys.exit(1)

def run_app():
    """Run the Flask application."""
    print("Starting Code Helper AI...")
    print("Access the application at http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server.")
    
    # Open the browser after a short delay
    def open_browser():
        sleep(2)
        webbrowser.open('http://127.0.0.1:5000')
    
    from threading import Thread
    browser_thread = Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Run the Flask app
    from app import app
    app.run(debug=True)

if __name__ == "__main__":
    check_python_version()
    check_api_key()
    install_dependencies()
    run_app()