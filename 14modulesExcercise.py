'''
Here we are going to put all the exercises about Modules
'''

print("------------ My solution. Modules Exercise 73 --------------------")

import math

answer = math.sqrt(15129)

print(answer)

print("------------ My solution. Modules Exercise 74 --------------------")
import keyword

def contains_keyword(anystring):
    return keyword.iskeyword(f"{anystring}")

print(contains_keyword("str"))

print("------------ COLT SOLUTION. Modules Exercise 74 --------------------")
import keyword

def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item):
            return True
    return False

print(contains_keyword("str", "if", "goodbay"))

print("------------ COLT SOLUTION. Modules Exercise 74 --------------------")

# # Archive helpers.py
# def lucky_number():
#     return 37
#
# #Archive exercise.py
# import helpers
# num = helpers.lucky_number()
