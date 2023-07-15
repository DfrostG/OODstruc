def vickrey_auction(bids):
    if len(bids) < 2:
        return "not enough bidder"
    
    sorted_bids = sorted(bids, reverse=True)
    highest_bid = sorted_bids[0]
    second_highest_bid = sorted_bids[1]

    if highest_bid == second_highest_bid:
        return "error : have more than one highest bid"
    
    winner_bid = highest_bid
    winner_payment = second_highest_bid

    return f"winner bid is {winner_bid} need to pay {winner_payment}"

bid_str = input("Enter All Bid : ")
bids = list(map(int, bid_str.split()))
result = vickrey_auction(bids)
print(result)