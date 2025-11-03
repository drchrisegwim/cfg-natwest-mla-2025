# GraphQL Exercise
This is a GraphQL exercise for the adaptive learning platform that generates personalized study paths for students based on their performance, learning style, and subject interests.

## Setup
### 1. Create and activate an isolated Python environment to manage dependencies.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 2. Install all dependencies required for both services.
```bash
pip install -r requirements.txt
```

### 3. Navigate to the learning content service folder and start the GraphQL server for learning content
```bash
cd learning_content_service
python app.py
```

### 4. Access the GraphiQL browser IDE
Open [http://127.0.0.1:5001/graphql](http://127.0.0.1:5001/graphql) in your browser.

### 5. Fetch all available learning modules with their details.
Run the following query in the GraphiQL browser IDE:
```graphql
{
    modules {
        moduleId
        topic
        difficulty
        learningStyle
        prerequisite
    }
}
```

### 6. Open a new terminal and activate the virtual environment.

Repeat step 1 in a new terminal window.

### 7. Navigate to the study path service folder and start the study path service.
```bash
cd study_path_service
python app.py
```

### 8. Sends a POST request with student performance, learning style, and interests.
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"student_performance\": {\"Algebra\": \"low\", \"Functions\": \"low\"}, \"learning_style\": \"Visual\", \"subject_interests\": [\"Mathematics\", \"Algebra\", \"Functions\"] }" http://127.0.0.1:5000/generate_path
```

### 9. Expected response of a generated study path. 
```json
{"personalized_path": ["M001", "M003", "M006"]}
```