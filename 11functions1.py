from random import random

def flip_coin():
    #generate random number 0-1
    r = random()
    print(r)
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"

def flip_coin1():
    #generate random number 0-1
    print(random())
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"


print(flip_coin())
print(flip_coin1())
