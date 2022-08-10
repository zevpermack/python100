import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = word_list[random.randint(0,len(word_list) - 1)]
print(f"chosen word for test: {chosen_word}")
word_len = len(chosen_word)

correct_guesses = []
for index in range(word_len):
  correct_guesses += "_"

while '_' in correct_guesses:
  guess = input("Guess a letter: ").lower()
  for index in range(0, word_len):
    if guess == chosen_word[index]:
      correct_guesses[index] = guess

print('you win')




print(correct_guesses)