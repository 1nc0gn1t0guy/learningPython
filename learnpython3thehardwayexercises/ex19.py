# this is a function, which can be called as many times as needed inside
# the script. This will need 2 values as an input.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("we can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("Or, we can use variables from our script:")
amount_of_cheese = 10
amout_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amout_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amout_of_crackers + 1000)