import os

bets_dictionary = {}
highest_bid = 0
winner = ""
continue_action = True
dictionary_position = 0

while continue_action == True:
    user_name = input("Introduce your name: ")
    user_bid = input("Introduce your bid: ")
    bets_dictionary[user_name] = user_bid

    action = input("Is there any other person? (yes/no)")

    if action == "no":
        continue_action = False
        os.system('cls')
        
    else:
        os.system('cls')

for bid in bets_dictionary:
    
    bid_amount = bets_dictionary[bid]
    

    if int(bid_amount) > highest_bid:
        highest_bid = int(bid_amount)
        winner = bid
        print(highest_bid)

    
print(winner, highest_bid)
