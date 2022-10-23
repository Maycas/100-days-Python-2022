import os
from art import LOGO

print(LOGO)

# Bid status variables
end_of_auction = False
bidders = []

def find_highest_bidder(bidder_list):
    max_bid = 0
    winner = ''
    for bidder in bidder_list:
        if bidder['bid'] > max_bid:
            winner = bidder['name']
            max_bid = bidder['bid']    
    print(f"The winner is {winner} with a bid of ${max_bid}")

# Collecting bids
while not end_of_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $")) 

    # store collected data
    bidders.append({
        "name": name,
        "bid": bid,
    })

    # check auction status - End or continue
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if should_continue == 'no':
        end_of_auction = True
        find_highest_bidder(bidders)
    else:
        # continue auction but hiding previous bids
        os.system('clear')