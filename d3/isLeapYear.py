print("--- is it a leap year? ---")

year = int(input("what year do you want to check? "))

if year % 4 == 0:
  if year % 100 != 0:
    print("This is a leap year")
  else:
    if year % 400 == 0:
      print("This is a leap year")
    else: 
      print("This is not a leap year")
else:
  print("This is not a leap year")
