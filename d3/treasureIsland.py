print("Welcome to Treasure Island. Your mission is to find the treasure")
q1 = input("L or R? ").lower()
if q1 != "l":
  print("Game Over")
else:
  q2 = input("Swim or Wait? ").lower()
  if q2 != "wait":
    print("Game Over")
  else:
    q3 = input("Which door, Red, Blue or Yellow? ").lower()
    if q3 != "yellow":
      print("Game Over")
    else: 
      print("You Win!")