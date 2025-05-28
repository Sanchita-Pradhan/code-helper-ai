from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure the Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("No API key found. Please set GEMINI_API_KEY in .env file")

genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_response():
    try:
        # Get data from request
        data = request.json
        
        # Extract all the inputs
        user_query = data.get('userQuery', '')
        programming_language = data.get('programmingLanguage', '')
        code_snippet = data.get('codeSnippet', '')
        desired_output = data.get('desiredOutput', '')
        code_context = data.get('codeContext', '')
        framework = data.get('framework', '')
        error_message = data.get('errorMessage', '')
        difficulty_level = data.get('difficultyLevel', 'Intermediate')
        
        # Construct prompt for Gemini
        prompt = f"""
        As a code helper AI, please assist with the following:
        
        User Query: {user_query}
        Programming Language: {programming_language}
        
        Code Snippet:
        ```{programming_language}
        {code_snippet}
        ```
        
        Desired Output/Goal: {desired_output}
        Code Context/File Type: {code_context}
        Framework/Library: {framework}
        
        Error Message (if any):
        {error_message}
        
        User Skill Level: {difficulty_level}
        
        Please provide a clear, concise solution with explanations appropriate for the user's skill level.
        Include code examples, potential issues, and best practices where relevant.
        """
        
        # Generate response from Gemini
        response = model.generate_content(prompt)
        
        # Return the response
        return jsonify({
            'success': True,
            'response': response.text
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)