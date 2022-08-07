print("Welcome to Odd/Even")

user_num = int(input("Which number do you want to check? \n"))%2

if user_num == 0:
  print("Your number is even!")
else:
  print("Your number is odd!")