import random

guess = input("Heads or Tails?\n").lower()
flip = random.random()
coin = ""
if flip > .5:
  coin = "tails"
  if guess == coin:
    print("Nice it was tails")
  else: 
    print("Sorry, it was tails")
else:
  coin = "heads"
  if guess == coin:
    print("Nice it was heads!")
  else:
    print("Sorry, it was heads")