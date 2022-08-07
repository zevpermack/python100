print("Welcome to Treasure Island. Your mission is to find the treasure")
q1 = input("L or R? ")
if q1 != "L":
  print("Game Over")
else:
  q2 = input("Swim or Wait? ")
  if q2 != "Wait":
    print("Game Over")
  else:
    q3 = input("Which door, Red, Blue or Yellow? ")
    if q3 != "Yellow":
      print("Game Over")
    else: 
      print("You Win!")