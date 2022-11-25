import random
import os
clear = lambda: os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def handle_input(user_input):
  if user_input == "y":
    return True
  else:
    return False

def assign_card():
  return random.choice(cards)

def deal_hand():
  card1 = assign_card()
  card2 = assign_card()
  return [card1, card2]

def calculate_hand_score(hand):
  sum_hand = sum(hand)
  if sum_hand > 21 and hand.count(11) > 0:
    for i in range(0, len(hand)):
      if hand[i] == 11:
        hand[i] = 1
        return sum(hand)
      
  return sum_hand
  

def ask_to_begin():
  return handle_input(input("would you like to play a hand of blackjack? 'y' = yes, 'n' = no: "))


def prompt_user(user_hand, user_score, computer_hand):
  print(f"Your cards: {user_hand}. Current score: {user_score}\nComputer's face up {computer_hand[1]}")
  if user_score == 21:
    print("I suggest you stay sir")
  return handle_input(input("y to hit, n to stay: "))


def play_blackjack():
  clear()
  print("""Welcome to blackjack.\n Rules:\n
  1. Aces will automatically be used as 11 or converted into 1 if hand goes over 21
  2. If you both blackjack from the start, you lose.
  3. Any other tie is a tie.
  4. GL you will need it""")
  user_hand = deal_hand()
  computer_hand = deal_hand()
  user_score = sum(user_hand)
  computer_score = sum(computer_hand)
  if user_score == 21 or computer_score == 21:
    if user_score == 21 and computer_score == 21:
      print("You both blackjacked but tie goes to the dealer :(")
    if user_score == 21:
      print(f"Boom, {user_hand} blackjack. You're a winner!!")
    elif computer_score == 21:
      print(f"Soz, computer blackjacked {computer_hand}. You lose :(")
    if ask_to_begin():
      play_blackjack()
  

  user_choice = prompt_user(user_hand, user_score, computer_hand)
  while user_choice:
    user_hand.append(assign_card())
    user_score = calculate_hand_score(user_hand)
    if user_score <= 21:
      user_choice = prompt_user(user_hand, user_score, computer_hand)
    else:
      return print(f"You bust with a hand of {user_hand} and a score of {user_score}, you lose!")
  
  while computer_score < 16:
    computer_hand.append(assign_card())
    computer_score = calculate_hand_score(computer_hand)
  
  if computer_score > 21:
    print(f"Nice you win with a hand of {user_hand} and a score of {user_score}.\nComputer busts with a hand of {computer_hand} and a score of {computer_score}.")
  else:
    if computer_score == user_score:
      return print(f"You tied with a hand of {user_hand} and a score of {user_score}.\nComputer had a hand of {computer_hand} also a score of {computer_score}.")
    elif computer_score > user_score:
      return print(f"You didn't gamble hard enough with a a hand of {user_hand} and a score of {user_score}.The computer had a hand of {computer_hand} and a score of {computer_score}.")
    else:
      return print(f"Nice, you're a gambling legend with a hand of {user_hand} and a score of {user_score}. The computer lost with a hand of {computer_hand} and a score of {computer_score}.")
  while ask_to_begin():
    play_blackjack()

while ask_to_begin():
  play_blackjack()

  

