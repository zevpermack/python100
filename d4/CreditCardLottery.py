import random

names_string = input("Provide a list of name to be chosen at random, separated by commas")
names = names_string.split(", ")
random_int = random.randint(1, len(names) - 1)

print(f"Sorry, {names[random_int]} you're paying ")
