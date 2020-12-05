'''
THe use of *args
'''
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(4,5,6,7,8))
print(sum_all_nums(4,3))

# Another example

def ensure_correct_info(*args):
    #print(args)
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Not sure who you are..."

print(ensure_correct_info()) # Not sure who you are...
print(ensure_correct_info("hello", False, 78))
ensure_correct_info(1, True, "Steele", "Colt")

# There's no need to call it arg
def sum_all_nums(*tits):
    total = 0
    for num in tits:
        total += tits
    return total

print(sum_all_nums(4,5,6,7,8))
print(sum_all_nums(4,3))

'''
THe use of **kwargs
'''
def fav_colors(**kwargs):
    #print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")

#Another exemple

def favorite_colors(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")

favorite_colors(rusty='green', colt='blue')
# rusty's favorite color is green
# colt's favorite color is blue


#Another exemple
def special_greeting(**kwargs):
    if "Colt" in kwargs and kwargs["Colt"] == "special":
        return "You get a special greeting Colt!"
    elif "Colt" in kwargs:
        return f"{kwargs["Colt"]} Colt!"

    return "Not sure who this is..."

special_greeting(Colt='Hello') # Hello Colt!
special_greeting(Bob='hello') # Not sure who this is...
special_greeting(Colt='special') # You get a special greeting Colt!
special_greeting(Heather="hello", Colt="special")

'''
ordering Parameters
'''
def display_info(a, b, *args, instructor="Colt", **kwargs):
    return [a, b, args, instructor, kwargs]
    print(args)
    print(type(args))

print(display_info(1, 2, 3, last_name="Steele", job="instructor"))

# Output function
# a - 1
# b - 2
# args(3)
# instructor - "Colt"
# kwargs - {"last_name": "Steele", "job": "Instructor"}
[1, 2, (3,), 'Colt', {'job': 'Instructor', 'last_name': 'Steele'}]

'''
Using * as an Argument:
Argument Unpacking
'''
def sum_all_values(*args):
    # there's a built in sum function - we'll see more later!
    return sum(args)

sum_all_values([1, 2, 3, 4]) # nope...
sum_all_values((1, 2, 3, 4)) # this does not work either...

sum_all_values(*[1, 2, 3, 4]) # 10
sum_all_values(*(1, 2, 3, 4)) # 10


'''
Using ** as an Argument:
Argument Unpacking
'''
def display_names(first, second):
    return f"{first} says hello to {second}"

names = {"first": "Colt", "second": "Rusty"}

display_names(names) # nope..

display_names(**names) "Colt says hello to Rusty"

#Another exemple
def add_and_multiply_numbers(a, b, c):
    print(a + b * c)

data = dict(a=1, b=2, c=3)

add_and_multiply_numbers(**data) # 7

#Another exemple
def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c)
    print("OTHER STUFF...")
    print(kwargs)

data = dict(a=1, b=2, c=3, d=77, name="Julio")

add_and_multiply_numbers(**data, cat="brown") # 7
