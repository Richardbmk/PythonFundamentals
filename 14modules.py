'''
Python Modules
'''
#Simple exemple

import random

print(random.choice(["apple", "banana", "cherry", "durian"]))
print(random.randint(1,100))

# Anothre exemple
import random as rand

print(rand.choice(["apple", "banana", "cherry", "durian"]))
print(rand.randint(1,100))
print(rand.shuffle(["apple", "banana", "cherry", "durian"]))

# Just choice what you need
from random import choice, randint, shuffle
print(choice(["apple", "banana", "cherry", "durian"]))
print(randint(1,100))

# To import everything
from random import *

#Choice what you need and chance the name
from random import choice as gimme_one, shuffle as mix_up_fruits

"""
Costumes Modules
"""
#Diferent file
def fn():
    return "do some stuff"

def other_fn():
    return "do some other stuff"

#THis is another file that i import the first file
import file1
file1.fn() # 'do some stuff'
file2.fn() # 'do some other stuff'

#if I only one to import one function
from bananas import dip_in_chocolate as dip
print(dip())

"""
Installing External Modules and  Termcolor
"""
import termcolor

print(dir(termcolor))
help(termcolor)
text = colored("HI THERE!", color="magenta", on_color="on_green", attrs=["blink"])
print(text)

"""
ASCII Art Exercise
"""
from pyfiglet import figlet_format
from termcolor import colored

# help(pyfiglet)
# help(pyfiglet.figlet_format)

print(figlet_format("Hi Richard"))
valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

msg = input("What would you like to print?")
color = input("What color? ")

if color not in valid_colors:
    color = "magenta"

ascii_art = figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)

"""
Using the autopep8 Package to clean up code
"""
# ugly code
import math, sys;

def example1():
    ####This is a long comment. This should be wrapped to fit within 72 characters.
    some_tuple=(   1,2, 3,'a'  );
    some_variable={'long':'Long code lines should be wrapped within 79 characters.',
    'other':[math.pi, 100,200,300,9876543210,'This is a long string that goes on'],
    'more':{'inner':'This whole logical line should be wrapped.',some_tuple:[1,
    20,300,40000,500000000,60000000000000000]}}
    return (some_tuple, some_variable)
def example2(): return {'has_key() is deprecated':True}.has_key({'f':2}.has_key(''));
class Example3(   object ):
    def __init__    ( self, bar ):
     #Comments should have a space after the hash.
     if bar : bar+=1;  bar=bar* bar   ; return bar
     else:
                    some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
                    return (sys.path, some_string)


# Cleaning up, using autopep8
                    # You can find the clean version in the archive 05ugly-code.py in this same carpet
                    # There's another option to do this while you write with subline text:
                            https://github.com/wistful/SublimeAutoPEP8
                    # Maybe you can fing a similar version for Atom
"""
The mystery of __name__variable
"""

# Look the video is complicated to explain
