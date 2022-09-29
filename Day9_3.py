from art9 import logo
#welcome logo
print(logo)
auction = {}

redo = True
while redo:
    name = input("What is your name? \n")
    bid = int(input ("What's your bid?\n"))
    auction[name] = bid
    restart = input("Are there any other bidder? type 'yes' or 'no'\n")
    if restart == 'no':
        redo = False
highest_bid = 0

for name,bid in auction.items():
    if bid > highest_bid:
        highest_bid = bid
        name_bid = name
print(f"{name_bid} wins the auction with a bid of {highest_bid}")
