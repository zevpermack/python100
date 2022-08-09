import random

key_codes = {
  "1": "Rock",
  "2": "Paper",
  "3": "Scissors"
}

ascii_art = {
  "1": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
  "2": '''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''',
  "3": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
}

player_choice = input("1 - Rock, 2 - Paper or 3 - Scissors? \n")
computer_choice = str(random.randint(1,3))

print(f"you chose {key_codes[player_choice]} \n {ascii_art[player_choice]}")
print(f"computer chose {key_codes[computer_choice]} \n {ascii_art[computer_choice]}")

if player_choice == computer_choice:
  print("It's a tie")

if player_choice == "1":
  if computer_choice == "2":
    print("You lose")
  if computer_choice == "3":
    print("You win")
if player_choice == "2":
  if computer_choice == "3":
    print("You lose")
  if computer_choice == "1":
    print("You win")
if player_choice == "3":
  if computer_choice == "1":
    print("You lose")
  if computer_choice == "2":
    print("You win")