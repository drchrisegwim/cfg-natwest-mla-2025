#Step 2: GREEN — Write minimum code to make it pass
#Now create the file: path_generator.py 

"""
Now we’ve made it pass, we can clean up.
we're not changing what it does still returns an empty list but, 
we are improving structure for future tests.
That’s the REFACTOR step. We always refactor when things are GREEN.
"""

class PathGenerator:
    def __init__(self, modules):
        self.modules = modules

    # code 1
    # def generate_path(self, student):
    #     # Just enough code to make the test pass
    #     return []
    
    # code 2

    def generate_path(self, student):
        suitable_modules = self._find_suitable_modules(student)
        if not suitable_modules:
            return []
        return []

    def _find_suitable_modules(self, student):
        # Placeholder helper method for future logic
        return []
    
    #Green step for matching_modules's case

    def generate_path(self, student):
        suitable_modules = [
        m["id"] for m in self.modules
        if m["learning_style"] == student.learning_style
        and any(topic in student.assessment_scores and student.assessment_scores[topic] == "low"
                for topic in m["topic"].split())
    ]
        return suitable_modules

