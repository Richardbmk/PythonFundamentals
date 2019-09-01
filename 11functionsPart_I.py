def sing_happy_birthday():
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print("Happy Birthday Dear You")
    print("Happy Birthday To You")

sing_happy_birthday()

#Key word return

def squeare_of_7():
    print("LIFE IS BETTER")
    return 7**2
result = squeare_of_7()
print(result)

def say_hi():
    return 'Hi!'

greeting = say_hi()

print(greeting) # 'Hi!'

# Exercise
def speak_pig():
    return "oink"

print(speak_pig())

# with one parameter
def square(num):
    return num * num

print(square(4))
print(square(8))

def sing_happy_birthday(name):
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print(f"Happy Birthday Dear {name}")
    print("Happy Birthday To You")

sing_happy_birthday("RIchard")

# Functions with parameters
def add(a,b):
    return a+b

def multiply(first, second):
    return first * second

#Naming parameters
def print_full_name(first_name, last_name):
    return(f"Your full name is {first_name} {last_name}")

# Parameter vs Argument
def divide(num1, num2):
    return num1/num2

print(divide(2/5))

# Exemple
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total
print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))

# Unnecessary "else"
def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:
        return False

def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False

# Default parameter
def exponent(num, power=2):
    return num ** power

print(exponent(2, 3)) # 8

# More Exemple
def add(a=10, b=20):
    return a+b

add() # 30
add(1,10) # 11

# More Exemple
def show_information(first_name="Colt", is_instructor=False):
    if first_name == "Colt" and is_instructor:
        return "Welcome back instructor Colt!"
    elif first_name == "Colt":
        return "I really thought you were an instructor..."
    return f"Hello {first_name}!"

show_information() # "I really thought you were an instructor..."
show_information(is_instructor=True) # "Welcome back instructor Colt!"
show_information('Molly') # Hello Molly!

# More Exemple
def add(a,b):
    return a+b

def math(a,b, fn=add):
    return fn(a,b)

def subtract(a,b):
    return a-b

math(2,2) # 4
math(2,2, subtract) # 0

# More Exemple
def math(fn=add, a,b,):
    return fn(a,b)
# This is not going to work. The order is importat.

# Key words arguments
def exponent(num, power=2):
    return num ** power

print(exponent(2, 3)) # 8
print(exponent(power=2, num=4)) # 64
print(exponent(num=4, power=2)) # 64

# Scope

    # Global variables
total = 0

def increment():
    total += 1
    return total

increment() # Error!
        #How to make it work!
total = 0

def increment():
    global total
    total += 1
    return total

increment() # 1

# NonLocal
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

# Documenting Functions

def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"

say_hello.__doc__ # 'A simple function that returns the string hello'
print.__doc__
random.randingt.__doc__
[1, 2, 3].pop.__doc__
