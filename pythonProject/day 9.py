
# BLIND BIDDING

bid = {}
Bidder = True
while (Bidder == True):
    name = input("Enter the bidders info: Mr.Ms.")
    bid_price = int(input("Enter the bidding price : $"))
    bid[name] = bid_price
    ask = input("Is there any other bidder:")
    if (ask == "yes"):

        Bidder = True

        print("\n" * 40)
    else:
        Bidder = False
        print("\n" * 20)

highest_bidder = max(bid, key=bid.get)
print(f"The highest bidder is {highest_bidder} with a bid of ${bid[highest_bidder]}")

