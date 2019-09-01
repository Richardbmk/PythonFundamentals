def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is Richard")

def rage():
    print("I HATE YOU!")

# We are decorating our functions
# greet = be_polite(greet)
# greet()
#
# polite_rage = be_polite(rage)
# polite_rage()

# Decorator Syntax, The right way to do a DECORATOR
@be_polite
def greet():
    print("My name is Richard")

# greet()


# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}"

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."
@shout
def lol():
    return "lol"


# print(greet("Ricardo"))
# print(order("rice", "fish"))
# print(order(main="rice", side="fish"))
# print(lol())

from functools import wraps
def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """ I AM WRAPPER FUNCTION """
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x, y):
    """ Adds two numbers together. """
    return x + y;

# print(add(10,30))

# print(add.__doc__)
# print(add.__name__)
# help(add)


# let's define a speed_test decorator
from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs) # Run the code function
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_nums_gen():
    return sum(x for x in range(10000))

@speed_test
def sum_nums_list():
    return sum([x for x in range(10000)])

print(sum_nums_gen())
print(sum_nums_list())
