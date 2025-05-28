# Code Helper AI

A web application that uses Google's Gemini 1.5 Flash model to provide coding assistance, explanations, and solutions to programming problems.

## Features

- Get help with coding issues across multiple programming languages
- Provide detailed context about your code and problem
- Receive tailored responses based on your skill level
- Code syntax highlighting for better readability
- Responsive design that works on desktop and mobile

## Prerequisites

- Python 3.7 or higher
- Google AI Studio API key for Gemini

## Installation

1. Clone this repository:

   ```
   git clone <repository-url>
   cd code-helper-AI
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Gemini API key:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

   You can obtain an API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Usage

### Local Development

1. Start the Flask development server:

   ```
   python run.py
   ```

2. Open your web browser and navigate to:

   ```
   http://127.0.0.1:5000
   ```

### Deployment to Render (Free Hosting)

1. Fork or clone this repository to your GitHub account
2. Sign up for a free account at [Render](https://render.com/)
3. Click "New +" and select "Web Service"
4. Connect your GitHub account and select this repository
5. Configure the service:
   - Name: code-helper-ai (or any name you prefer)
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Add the environment variable:
   - Key: `GEMINI_API_KEY`
   - Value: Your Google Gemini API key
7. Click "Create Web Service"

Your application will be deployed and accessible via a URL like: `https://code-helper-ai.onrender.com`

3. Fill out the form with your coding question or issue:
   - Enter your query or problem statement
   - Select the programming language
   - Paste your code snippet (if applicable)
   - Provide additional context as needed
   - Submit the form to get AI-generated assistance

## Project Structure

```
code-helper-AI/
├── app.py                 # Flask application and API endpoints
├── run.py                 # Script to run the application locally
├── run.bat                # Batch file to run the application on Windows
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── gunicorn.conf.py       # Gunicorn configuration for production
├── render.yaml            # Render deployment configuration
├── static/
│   ├── css/
│   │   └── style.css      # Application styling
│   └── js/
│       └── script.js      # Client-side JavaScript
└── templates/
    └── index.html         # Main HTML template
```

## Customization

- Modify `static/css/style.css` to change the application's appearance
- Adjust the prompt template in `app.py` to customize how queries are sent to Gemini
- Edit `templates/index.html` to add or remove form fields

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Google Generative AI](https://ai.google.dev/) for the Gemini API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [highlight.js](https://highlightjs.org/) for code syntax highlighting
- [marked.js](https://marked.js.org/) for Markdown rendering
