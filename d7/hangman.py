import random
import os
from gameInfo import stages, word_list

lives = 6
prev_guesses = {}
chosen_word = word_list[random.randint(0,len(word_list) - 1)]
word_len = len(chosen_word)

correct_guesses = []
for index in range(word_len):
  correct_guesses += "_"
print(correct_guesses)

game_over = False

while not game_over:
  guess = input("Guess a letter: ").lower()
  os.system('cls' if os.name == 'nt' else 'clear')
  if prev_guesses.get(guess):
    print(f"You already guessed {guess}")
  else:
    prev_guesses[guess] = True
  for index in range(0, word_len):
    if guess == chosen_word[index]:
      correct_guesses[index] = guess
  print(correct_guesses)
  if guess not in correct_guesses:
    print(f"{guess} is not in the word")
    lives -= 1
    print(f"- - - - - \n {lives} lives left")
    print(f"{stages[lives]}")

  if '_' not in correct_guesses:
    game_over = True
    print('you win')
  if lives == 0:
    game_over = True
    print('you lose')
