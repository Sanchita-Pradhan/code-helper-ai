# Code Helper AI

A local application that uses Google's Gemini 1.5 Flash model to provide coding assistance, explanations, and solutions to programming problems.

## Features

- Get help with coding issues across multiple programming languages
- Provide detailed context about your code and problem
- Receive tailored responses based on your skill level
- Code syntax highlighting for better readability
- Runs completely locally on your computer

## Prerequisites

- Python 3.7 or higher
- Google AI Studio API key for Gemini

## Installation

1. Make sure you have Python installed on your computer

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Make sure your `.env` file in the project root has your Gemini API key:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

   You can obtain an API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Running the Application

### Option 1: Using the Batch File (Easiest)

1. Simply double-click the `run_app.bat` file in the project folder
2. The application will start automatically
3. Your default web browser will open to http://127.0.0.1:5000
4. When you're done, close the command prompt window

### Option 2: Using Command Line

1. Open a command prompt
2. Navigate to the project directory
3. Run the following command:

   ```
   python app.py
   ```

4. Open your web browser and go to http://127.0.0.1:5000

## Using the Application

1. Fill out the form with your coding question or issue:

   - Enter your query or problem statement
   - Select the programming language
   - Paste your code snippet (if applicable)
   - Provide additional context as needed
   - Click "Get Help" to get AI-generated assistance

2. The AI will analyze your query and provide:

   - Explanations of your code issues
   - Suggested solutions
   - Code examples
   - Best practices

3. When you're done, simply close the browser tab and the command prompt window

## Project Structure

```
code-helper-AI/
├── app.py                 # Flask application and API endpoints
├── run_app.bat            # Batch file to run the application on Windows
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── static/
│   ├── css/
│   │   └── style.css      # Application styling
│   └── js/
│       └── script.js      # Client-side JavaScript
└── templates/
    └── index.html         # Main HTML template
```

## Notes

- This application runs completely locally on your computer
- No data is sent to external servers except to Google's Gemini API for processing your queries
- Your Gemini API key is stored in the `.env` file and is only used to authenticate with Google's API

## Acknowledgements

- [Google Generative AI](https://ai.google.dev/) for the Gemini API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [highlight.js](https://highlightjs.org/) for code syntax highlighting
- [marked.js](https://marked.js.org/) for Markdown rendering
