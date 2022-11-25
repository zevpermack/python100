def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def get_operator():
  for operation in operations:
    print(operation)

  return input("Pick an operation symbol from the list above: ")

def get_second_number():
  return int(input("What's the second number?: "))

def finish_equation():
  symbol = get_operator()
  num2 = get_second_number()
  return symbol, num2

def calculate(symbol, num1, num2):
  return operations[symbol](num1, num2)

def continue_calculating(previous_result): 
  user_answer = input(f"Would you like to continue calculating on your previous result {previous_result}? 'y' for yes. 'n' for no: ")
  if user_answer == "y":
    return True
  return False

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("What's the first number?: "))

symbol, num2 = finish_equation()

curr_result = calculate(symbol, num1, num2)
print(curr_result)

switch = continue_calculating(curr_result)
while switch:
  symbol, num2 = finish_equation()
  curr_result = calculate(symbol, curr_result, num2)
  print(curr_result)
  switch = continue_calculating(curr_result)

print("See ya!")


