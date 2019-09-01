#Exercise
print("-------- My Solution -----------")
# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
print(food)
#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
for k,v in bakery_stock.items():
    if food in k:
        print(f"There are {v} {k}")
    elif k not in food:
        print("We don't make that sorry")

print("-------- COLT SOLUTION 1 -----------")

if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")


print("-------- COLT SOLUTION 2 -----------")

quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")
