print("-------THE SIMPLE POSIBLE SOLUTION BY COLT------")
from random import randint
number = randint(1, 10)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if number > int(guess):
        print("To low, try again")
    elif number < int(guess):
        print("To high, try again")
    else:
        print("You gessed it! You won...")
print(number)
