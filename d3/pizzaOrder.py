print("Welcome to pizza deliveries!")
size = input("What size pizza do you want? S, M, L \n")
add_pep = input("Do you want to add pepperoni? Y, N \n")
extra_cheese = input("Do you want to add extra cheese? Y, N \n")

bill = 0

if size == "S":
  bill += 15
  if add_pep == "Y":
    bill += 2
elif size == "M":
  bill +=20
  if add_pep == "Y":
    bill += 3
else:
  bill +=25
  if add_pep == "Y":
    bill +=3

if extra_cheese == "Y":
  bill += 1


print(f"Your final bill is {bill}")