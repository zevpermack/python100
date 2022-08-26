#Write your code below this line 👇

def prime_checker(number):
  is_prime = True

  for denominator in range(2, number):
    if number%denominator == 0:
      is_prime = False
  
  if is_prime:
    print("It's prime baby")
  else:
    print("It ain't prime")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)