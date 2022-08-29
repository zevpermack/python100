def score_eval(score):
  if score >= 91: 
   return "Outstanding"
  elif score >= 81:
   return "Exceeds Expectations"
  elif score >= 71:
   return "Acceptable"
  else:
    return "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}


for student in student_scores:
  student_score = student_scores[student]
  student_grades[student] = score_eval(student_score)

print(student_grades)