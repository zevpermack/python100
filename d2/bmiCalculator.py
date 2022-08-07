height = float(input("Please enter your height in meters: \n"))
weight = float(input("Please enter your weight in kg: \n"))

#Makes a whole number for your BMI instead of floating point but it just chops it and doesn't round
bmi = int(weight/height**2)

print("Your BMI is: " + str(bmi))