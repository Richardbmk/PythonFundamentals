# While loops Exiercise

from random import randint

number = randint(1, 10)
print(number)
i = 0
while number != 5:
    i += number
    number = randint(1, 10)
    print(number)
