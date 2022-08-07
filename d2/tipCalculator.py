print("Welcome to the tip calculator!")

total = float(input("What is the total bill? \n"))
tip_percentage = float(input("What percent would you like to tip? \n"))
people = int(input("How many people are splitting the bill? \n"))

amount_per_person = "{:.2f}".format((total + (total * tip_percentage/100)) / people)

final_msg = f"Each person owes ${amount_per_person}"
print(final_msg)