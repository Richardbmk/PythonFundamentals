
# Exercise show_args COLT SOLUTION
""" Write a function called show_args which accepts a function and
returns another function. Before invoking the function passed to it,
show_args should be responsable for printing two things:
1. A tuple of the positional arguments
2. A dictionary of the keywords arguments"""

from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs", kwargs)
        return fn(*args, **kwargs)
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass


# do_nothing(1, 2, 3, a="hi", b="bye")

# Exemple. 285. Another Example: Ensuring Args With A Decorator

from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! sorry :(")
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"hi there {name}")

# print(greet("McFly")) # It works
# print(greet(name="McFly")) # It doesn't work, becouse with didn't allowed it.


# Exercise double_return a mix of my SOLUTION and COLT SOLUTION
""" Write a function called double_return which accepts a function and
return another function. double_return should decorate a function by
returning two copies of the inner function's return value inside
of a list """

from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

@double_return
def add(x, y):
    return x + y

@double_return
def greet(name):
    return "Hi, I'm " + name


# print(add(1, 2)) # [3, 3]
# print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]

# Exercise ensure_fewer_than_three_args
""" Write a function called ensure_fewer_than_three_args which accepts
a functionand returns another function. The function passed  to it should
only be invoked if there are fewer than three positional arguments passed to it.
Otherwise, the inner function should return "Too many arguments!" """

from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) >= 3:
            raise ValueError("Too many arguments!")
        return fn(*args, **kwargs)
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

# print(add_all()) # 0
# print(add_all(1)) # 1
# print(add_all(1,2)) # 3
# print(add_all(1,2,3)) # "Too many arguments!"

# Exercise only_ints
""" Write a function called only inst which accepts a function
and return another funciont. The function passed to it should only be
invoked if all of the arguments passed to it are integers.
Otherwise the inner function should return
 "Please only invoke with integers" """

# Colt solutoin
from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([args for arg in args if type(arg) != int]):
            return ValueError("Please only invoke with integers")
        return fn(*args, **kwargs)
    return inner

# # Nickolay solution
# from functools import wraps
#
# def only_ints(fn):
#     @wraps(fn)
#     def wrapper(*args):
#         int_check = all(type(i) == int for i in args)
#         if int_check:
#             return fn(*args)
#         return "Please only invoke with integers."
#     return wrapper


@only_ints
def add(x, y):
    return x + y

# print(add(1, 2)) # 3
# print(add("1", "2")) # "Please only invoke with integers."


# Exercise only_ints
""" Write a function called ensure_authorized which accepts a function
and returns another function. The functions passed to it should be
invoked if there exists a keywords arguments with a name of "role"
and a value of "admin". Otherwise, the inner function should
return "Unauthorized" """

# Colt solutions
from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def person(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return person


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

# print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
# show_secrets(role="nobody") # "Unauthorized"
# show_secrets(a="b") # "Unauthorized"

# Exemples. 290. Writing an ensure_first_arg_is Decorator
from functools import wraps

@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito", "ice cream"))
print(fav_foods("ice cream", "burrito"))

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10, 12))
print(add_to_ten(1, 2))
