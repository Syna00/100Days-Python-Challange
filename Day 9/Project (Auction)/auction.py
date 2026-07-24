from art import logo
print(logo)


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"Pemenangnya adalah {winner} dengan melelang sebesar Rp.{highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("Siapa nama kamu? \n")
    price = int(input("Masukkan harga lelang kamu : \n"))
    bids[name] = price
    should_continue = input("Apakah ada yang mau melakukan lelang lagi? Ketik 'ya' atau 'tidak' : \n").lower()
    if should_continue == "tidak":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "ya":
        print("\n" * 10)



