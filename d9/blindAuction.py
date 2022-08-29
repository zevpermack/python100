import os



bids = {}

def add_bid():
  name = input("what is your name? ")
  bid = int(input("what is your bid in dollars? "))
  bids[name] = bid
  run_again = input("do you want to add another bidder (yes or no)? ").lower()
  if run_again == "yes":
    os.system('cls' if os.name == 'nt' else 'clear')
    add_bid()
  

def print_winner(bidding_record):
  os.system('cls' if os.name == 'nt' else 'clear')
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    if bidding_record[bidder] > highest_bid:
      highest_bid = bidding_record[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of {bidding_record[winner]}")
    
add_bid()
print_winner(bids)

