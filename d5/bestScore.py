scores = input("What are the scores in the class?\n ").split(",")

max_score = 0 

for score in scores:
  int_score = int(score)
  if int_score > max_score:
    max_score = int_score

print(f"max score is {max_score}")