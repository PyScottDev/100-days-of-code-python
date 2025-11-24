from ASCII_art import gavel_logo

print(gavel_logo)

bids_made = {}


def bid_calculator (bids_made):
    highest_bid = -1
    winners_name = ""
    for name in bids_made:
        amount = bids_made[name]
        if amount > highest_bid:
            highest_bid = amount
            winners_name = name

    print(f"The highest bidder is {winners_name} with a bid of £{highest_bid}")

cont_auction = "Y" 

while cont_auction == "Y":
    name = input("What is you name?\n")
    bid = int(input("What is you bid?\n£"))
    #bids_made = {}
    bids_made[name] = bid
    cont_auction = input("Are there any other bidders? 'Y' for yes and 'N' for no\n").upper()
    if cont_auction == "Y":
        print("\n" * 100)
    else:
        bid_calculator(bids_made)
    



