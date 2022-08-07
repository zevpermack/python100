height = float(input("What is your height in m: "))
weight = float(input("What is your weight in kg: "))

bmi = round(weight/height**2)
print(f"Your BMI is {bmi}")

if bmi > 35:
  print("You are clinically obese")
elif bmi > 30:
  print("You are obese")
elif bmi > 25:
  print("You are overweight")
elif bmi > 18.5:
  print("You are a normal weight")
else:
  print("You are underweight")



