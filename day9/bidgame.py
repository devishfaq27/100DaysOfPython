# TODO-1: Ask the user for inputs
#TODO-2: save the data into a dictinory {name: price}
# TODO-3: weather if new bid added
#TODO-4:  compaire the bids into dictionaries



# def finding_highest_bidder(bid_dictionary):
#     high_bid = 0
#     winner = ""
#     for bidder in bid_dictionary:
#         bid_amount = bid_dictionary[bidder]
#         if bid_amount > high_bid:
#             high_bid = bid_amount
#             winner = bidder
#     print(f"the high bidder is {winner} and the bid is {high_bid}")
#
#
# bids = {}
#
#
# should_continue = True
# while should_continue:
#     name = input("what is your name: ")
#     price = int(input("how much bid you want: $"))
#     bids[name] = price
#     restart = input("Is there any more who want to bid: ")
#     if restart == "no":
#         should_continue = False
#         finding_highest_bidder(bids)
#
#
#






















# def find_highest_bid(bidding_dictionary):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#
#     print(f"{winner} {highest_bid}")
#
#
# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("Enter your name: ")
#     price = int(input("Enter your bid price: $"))
#     bids[name] = price
#     should_continue = input("are there any other biddes type 'yes' or 'no' \n")
#     if should_continue == "no":
#         find_highest_bid(bids)


