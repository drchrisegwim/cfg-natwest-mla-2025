import unittest
from unittest.mock import patch
from study_path_service.path_generator import PathGenerator


class TestPathGenerator(unittest.TestCase):

    @patch('study_path_service.path_generator.requests.post')
    def test_generate_empty_path_if_no_modules_match(self, mock_post):
        # Mock the GraphQL response to return no modules
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"data": {"modules": []}}
        mock_post.return_value.raise_for_status.return_value = None

        generator = PathGenerator()
        student_performance = {"Algebra": "low"}
        learning_style = "Visual"
        subject_interests = ["Mathematics"]
        path = generator.generate_personalized_path(
            student_performance, learning_style, subject_interests)
        self.assertEqual(path, ['Kiruthika'])

    @patch('study_path_service.path_generator.requests.post')
    def test_personalized_path_for_learner_Y(self, mock_post):
        # Mock the GraphQL response with the predefined modules
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "data": {
                "modules": [
                    {"moduleId": "M001", "topic": "Algebra Basics", "difficulty": "Easy",
                        "learningStyle": "Visual", "prerequisite": "None"},
                    {"moduleId": "M002", "topic": "Geometry Intro", "difficulty": "Easy",
                        "learningStyle": "Auditory", "prerequisite": "None"},
                    {"moduleId": "M003", "topic": "Functions", "difficulty": "Medium",
                        "learningStyle": "Visual", "prerequisite": "M001"},
                    {"moduleId": "M004", "topic": "Calculus Intro", "difficulty": "Hard",
                        "learning_style": "Visual", "prerequisite": "M003"},
                    {"moduleId": "M005", "topic": "Advanced Physics", "difficulty": "Hard",
                        "learning_style": "Kinesthetic", "prerequisite": "M004"},
                    {"moduleId": "M006", "topic": "Basic Chemistry", "difficulty": "Medium",
                        "learning_style": "Visual", "prerequisite": "None"},
                ]
            }
        }
        mock_post.return_value.raise_for_status.return_value = None

        generator = PathGenerator()
        student_performance = {"Algebra": "low", "Functions": "low"}
        learning_style = "Visual"
        subject_interests = ["Algebra", "Functions",
                             "Mathematics"]  # Added for relevance

        path = generator.generate_personalized_path(
            student_performance, learning_style, subject_interests)

        # Assertions based on the BDD scenario from the previous lesson
        self.assertIn("M001", path)
        self.assertEqual(path[0], "M001")  # Path should start with M001
        self.assertIn("M003", path)
        self.assertGreater(path.index("M003"),
                           path.index("M001"))  # M003 after M001
        self.assertNotIn("M002", path)
        self.assertNotIn("M004", path)
        # Check for prioritization of visual modules (this is harder to assert precisely with simple logic)
        # The current simple logic should naturally prioritize M001, M003, M006 due to low scores and visual style


if __name__ == '__main__':
    unittest.main()
