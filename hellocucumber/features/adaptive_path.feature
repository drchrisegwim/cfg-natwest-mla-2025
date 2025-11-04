Feature: Personalised Study Path
  This is a cucumber project with a Scenario for an adaptive learner journey 
Scenario: Visual learner with low Algebra and Functions
  Given a new student "learner Y" with a "visual" learning style
  And they complete an initial assessment with "low" scores in "Algebra" and "Functions"
  When a study path is beign generated Thirtha
  Then the first module should be "M001"
  And the next module should be "M003"
  And the path should not include "M002"
  And the path should not include "M004"
  And the path should prefer modules with style "visual"



  