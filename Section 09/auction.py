from art import logo
print(logo)

def cls():
    print("\n" * 20)

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}! Sold!")

while not bidding_finished:
    name = input("What is your name: ")
    price = int(input("What's your bid: $"))
    bids[name] = price
    should_continue = input("Are there any other bids? Type 'yes' or 'no' ")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        cls()



