#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

ordered_password = ""
for i in range(0, nr_letters):
  random_index = random.randint(0,len(letters) - 1)
  ordered_password += letters[random_index]
for i in range(0, nr_symbols):
  random_index = random.randint(0,len(symbols) - 1)
  ordered_password += symbols[random_index]
for i in range(0, nr_numbers):
  random_index = random.randint(0,len(numbers) - 1)
  ordered_password += numbers[random_index]

scrambled_pass = ""

for i in range(0, len(ordered_password)):
  index = random.randint(0, len(ordered_password) - 1)
  scrambled_pass += ordered_password[index]
  ordered_password = ordered_password[:index] + ordered_password[index+1:]

print(scrambled_pass)



