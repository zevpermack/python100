alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  new_msg = ""
  if shift > 25:
    shift = shift % 25
  if direction == "decode":
    shift *= -1
  for char in text:
    if char in alphabet:
      letter_index = alphabet.index(char)
      new_index = letter_index + shift
      if new_index >= 26:
        new_index = new_index - 26
      if new_index < 0:
        new_index = new_index + 26
      new_msg += alphabet[new_index]  
    else:
      new_msg += char
  
  print(f"Your {direction}d string is {new_msg}")

def run():

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  run_again = input("Do you want to run the cypher again?\n")
  if run_again == "yes":
    run()
  print("Goodbye")

run()


