# Exemples. 290. Writing an ensure_first_arg_is Decorator
def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner

from functools import wraps

@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

# print(fav_foods("burrito", "ice cream"))
# print(fav_foods("ice cream", "burrito"))

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

# print(add_to_ten(10, 12))
# print(add_to_ten(1, 2))
"""
# NOT WORKING CODE. THE PORPOURSE IS ONLY TO EXPLAIN THIS FILE.

# Wen we write:
@decorator
def func(*args, **kwargs):
    pass
# we are really doing:
func = decorator(func)

# When we write:
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass
# we're really doing:

func = decorator_with_args(arg)(func)
"""

# 291. Enforcing Argument Types With A Decorator
def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #Convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def divide(a,b):
    print(a/b)

print(divide("5","2"))
print(repeat_msg("Winner", "3"))


# Exercise delay
""" Write a function called delay which accepts a time and return an inner
function that accepts a function. When used as decorator, delay will wait
to execute the function being decorated by the
amount of time passed into it. Before starting the timer, delay will also print
a message informing the user that there will be delay before the decorated
function gets run. """

from functools import wraps
from time import sleep

def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"waiting {timer}s before running {fn.__name__s}")
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner


@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
