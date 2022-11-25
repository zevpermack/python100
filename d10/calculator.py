def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for operation in operations:
  print(operation)

symbol = input("Pick an operation symbol: ")
answer = num1 
print(operations[symbol](num1, num2))