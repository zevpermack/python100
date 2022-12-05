import random

random_number = random.randint(0, 100)
game_over = False

print(f'Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')
dev = input("Are you dev checking the game? \"y\" or \"n\": ")
if dev == "y":
  print(f"The correct answer is: {random_number}")

mode = input("Choose a difficult. Type 'easy' or 'hard': ")
lives = 10 if mode == 'easy' else 5
print(f"You have {lives} lives")


while(game_over != True):
  if(lives == 0):
    print("You are out of lives better luck next time")
    break
  guess = int(input("Make a guess: "))
  if guess != random_number:
    if guess > random_number:
      print("Too high try again")
    elif guess < random_number: 
      print("Too low try again")
    lives -= 1
    print(f"you have {lives} lives left")
  else:
    game_over = True
    print(f"You dunnit! The number was {random_number}")

  


