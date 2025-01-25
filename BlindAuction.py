# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)


def highest_bid(bidding_record):
    highestbid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highestbid:
            highestbid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with the bid of {highestbid}")


bids = {}

continue_bid = True

while continue_bid:
    name = input("enter your name: ")
    amount = int(input("enter your amount you want to bid: $"))
    bids[name] = amount
    should_continue = input("do you want to continue? 'yes' or 'no' : ").lower()
    if should_continue == 'no':
        continue_bid = False
        highest_bid(bids)

    elif should_continue =="yes":
        print("\n" *30)



