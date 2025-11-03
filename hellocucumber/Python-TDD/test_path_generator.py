    # Step 1: RED — Write a failing test


import unittest
from unittest.mock import MagicMock

class TestPathGenerator(unittest.TestCase):
    

    def setUp(self):
        self.student_sarah = MagicMock(
            student_id="sarah123",
            learning_style="visual",
            assessment_scores={"Algebra": "low", "Functions": "low", "Geometry": "high"}
        )

        self.available_modules = [
            {"id": "M001", "topic": "Algebra Basics", "difficulty": "Easy", "learning_style": "visual", "prerequisite": None},
            {"id": "M002", "topic": "Geometry Intro", "difficulty": "Easy", "learning_style": "auditory", "prerequisite": None},
            {"id": "M003", "topic": "Functions", "difficulty": "Medium", "learning_style": "visual", "prerequisite": "M001"},
        ]

    '''
       Step 1 in TDD is to write a test for behavior we want, but don’t have yet.
        Check following test that says:
        if a student asks for a subject we don’t have (like History), the generator should return an empty list.
        But PathGenerator doesn’t even exist yet! So this test will fail ----> tha
    '''

    def test_generate_path_no_suitable_modules(self):  # make sure this is inside the class
        student_chris = MagicMock(
            student_id="chris789",
            learning_style="auditory",
            assessment_scores={"History": "low"}
        )
        self.fail("PathGenerator not yet implemented or does not return empty list for no matches")

# run the test case :- python3 -m unittest test_path_generator.py



#Step 2: GREEN — Write minimum code to make it(test) pass
#Now create the file: path_generator.py 


import unittest
from unittest.mock import MagicMock
from path_generator import PathGenerator  #PathGenerator will give us an empty list

class TestPathGenerator(unittest.TestCase):

    def setUp(self):
        self.student_sarah = MagicMock(
            student_id="sarah123",
            learning_style="visual",
            assessment_scores={"Algebra": "low", "Functions": "low", "Geometry": "high"}
        )

        self.available_modules = [
            {"id": "M001", "topic": "Algebra Basics", "difficulty": "Easy", "learning_style": "visual", "prerequisite": None},
            {"id": "M002", "topic": "Geometry Intro", "difficulty": "Easy", "learning_style": "auditory", "prerequisite": None},
            {"id": "M003", "topic": "Functions", "difficulty": "Medium", "learning_style": "visual", "prerequisite": "M001"},
        ]
   

    def test_generate_path_no_suitable_modules(self):  # make sure this is inside the class
        student_chris = MagicMock(
            student_id="chris789",
            learning_style="auditory",
            assessment_scores={"History": "low"}
        )

        generator = PathGenerator(self.available_modules)
        path = generator.generate_path(student_chris)
        self.assertEqual(path, [])  # test the expected empty list


        """
        Now we’ll add a new test for the next feature:
        When Sarah (a visual learner) has low Algebra and Functions scores,
        she should get modules M001 and M003.
        This test will fail because our PathGenerator isn’t that smart yet.
        """

        # step1 : red

    def test_generate_path_with_matching_modules_and_style(self):
        generator = PathGenerator(self.available_modules)
        path = generator.generate_path(self.student_sarah)

        expected_path = ["M001", "M003"]  # Visual learner, low Algebra/Functions
        self.assertEqual(path, expected_path)

