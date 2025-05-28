document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('codeHelperForm');
    const submitBtn = document.getElementById('submitBtn');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const responseContainer = document.getElementById('responseContainer');

    // Function to render markdown with code highlighting
    function renderMarkdown(text) {
        // Configure marked to use highlight.js for code highlighting
        marked.setOptions({
            highlight: function(code, lang) {
                if (lang && hljs.getLanguage(lang)) {
                    return hljs.highlight(code, { language: lang }).value;
                }
                return hljs.highlightAuto(code).value;
            },
            breaks: true
        });

        return marked.parse(text);
    }

    // Handle form submission
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Show loading indicator and disable submit button
        loadingIndicator.classList.remove('hidden');
        submitBtn.disabled = true;
        responseContainer.innerHTML = '';
        
        // Collect form data
        const formData = {
            userQuery: document.getElementById('userQuery').value,
            programmingLanguage: document.getElementById('programmingLanguage').value,
            codeSnippet: document.getElementById('codeSnippet').value,
            desiredOutput: document.getElementById('desiredOutput').value,
            codeContext: document.getElementById('codeContext').value,
            framework: document.getElementById('framework').value,
            errorMessage: document.getElementById('errorMessage').value,
            difficultyLevel: document.getElementById('difficultyLevel').value
        };
        
        try {
            // Send request to backend
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            if (data.success) {
                // Process and display the response
                const formattedResponse = renderMarkdown(data.response);
                responseContainer.innerHTML = formattedResponse;
                
                // Apply syntax highlighting to code blocks
                document.querySelectorAll('pre code').forEach((block) => {
                    hljs.highlightBlock(block);
                });
            } else {
                // Display error message
                responseContainer.innerHTML = `
                    <div style="color: var(--error-color);">
                        <h3>Error</h3>
                        <p>${data.error || 'An error occurred while generating the response.'}</p>
                    </div>
                `;
            }
        } catch (error) {
            // Handle network or other errors
            responseContainer.innerHTML = `
                <div style="color: var(--error-color);">
                    <h3>Error</h3>
                    <p>Failed to connect to the server. Please try again later.</p>
                    <p>Details: ${error.message}</p>
                </div>
            `;
        } finally {
            // Hide loading indicator and re-enable submit button
            loadingIndicator.classList.add('hidden');
            submitBtn.disabled = false;
        }
    });
});