from flask import Flask, request, jsonify
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from study_path_service.path_generator import PathGenerator

app = Flask(__name__)
generator = PathGenerator()

@app.route('/generate_path', methods=['POST'])
def generate_path():
    data = request.json
    student_performance = data.get('student_performance', {})
    learning_style = data.get('learning_style')
    subject_interests = data.get('subject_interests', [])

    if not all([student_performance, learning_style, subject_interests]):
        return jsonify({"error": "Missing required data: student_performance, learning_style, or subject_interests"}), 400

    # you can un-comment to change between calling one of 2 functions either _fetch_all_modules or generate_personalized_path

    # path = generator._fetch_all_modules()
    path = generator.generate_personalized_path(student_performance, learning_style, subject_interests)
    return jsonify({"personalized_path": path})

if __name__ == '__main__':
    app.run(port=5000)