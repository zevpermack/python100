print("Welcome to love calculator")

name1 = input("What is your name? ").lower()
name2 = input("What is your crushes name? ").lower()
combined_name = name1+name2
first_digit = 0
second_digit = 0

first_digit += combined_name.count("t")
first_digit += combined_name.count("r")
first_digit += combined_name.count("u")
first_digit += combined_name.count("e")


second_digit += combined_name.count("l")
second_digit += combined_name.count("o")
second_digit += combined_name.count("v")
second_digit += combined_name.count("e")

love_score = str(first_digit) + str(second_digit)
love_score_int = int(love_score)

if love_score_int < 10 or love_score_int > 90:
  print(f"Your love score is {love_score}, you go together like coke and mentos")
elif love_score_int > 40 and love_score_int < 50:
  print(f"Your love score is {love_score}, you are alright together")
else:
  print(f"Your love score is {love_score}")



