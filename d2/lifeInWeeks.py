age = int(input("how old are you? \n"))

days_left = 90 * 365 - age * 365
weeks_left = 90 * 52 - age * 52
months_left = 90 * 12 - age * 12


print(f"you have {days_left} days {weeks_left} weeks and {months_left} months left to live ")