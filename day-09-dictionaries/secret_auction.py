import art
import os

print(art.logo)
print("Welcome to the secret auction program.")

finish = False

bids = {}

while not finish:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid

    result = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    while result != 'yes' and result != 'no':
        result = input("Please, type 'yes' or 'no'.\n")
    if result == 'no':
        finish = True
    os.system("clear")

highest_bidder = ""
highest_bid = 0

for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
