'''
Common Types of
Errors in Python
'''
 # Sintaxys Errors
 def first: # SyntaxError
None = 1 # SyntaxError
return # SyntaxError

#NameError
test # NameError: name 'test' is not defined

#TypeError
len(5)
# TypeError: object of type 'int' has no len()
"awesome" + []
# TypeError: cannot concatenate 'str' and 'list' objects

#IndexError
list = ["hello"]
list[2] # IndexError: list index out of range

#ValueError
int("foo") # ValueError: invalid literal for int() with base 10: 'foo'

#KeyError
d = {}
d["foo"] # KeyError: 'foo'

#AtributeError
"awesome".foo # AttributeError: 'str' object has no attribute 'foo'


'''
Raising Our own Error message
'''
raise ValueError('invalid value')

#Exemple 1
def colorize(text, color):
    colors = ["cyan", "yellow", "blue", "green", "magenta"]
    if type(color) in not str:
        raise TypeError("text must be instace of str")
    if type(text) is not str:
        raise TypeError("text must be instace of str")
    if color not in colors:
        raise ValueError("Color is invalid color")
    print(f"printed {text} in {color}")

colorize("hello", "red")
colorize(34, "red")


'''
Handle Errors
Try and Except Blocks
'''
#Simple exemple
try:
    foobar
except:
    print("PROBLEM!")
print("after the try")

#Improved version
try:
    colt
except NameError:
    print("You tried to use a variable that was never declared!")

#Another good exemple

d = {"name": "Ricky"}
d["city"] # KeyError
get(d, "name")

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

d = {"name": "Ricky"}
print(get(d, "name"))
print(get(d, "city"))

'''
Try, Except, Else and Finally
'''
#Exemple 1
try:
    num = int(input("please enter a number: "))
except:
    print("That's not a number!")
else:
    print("I'M IN THE ELSE!")
finally:
    print("RUNS NO MATTER WHAT")

#Exemple 2
while True:
    try:
        num = int(input("please enter a number: "))
    except:
        print("That's not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("RUNS NO MATTER WHAT")
print("REST OF THE GAME LOGIC!")

#Exemple 2.1. Improved
while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("RUNS NO MATTER WHAT")
print("REST OF THE GAME LOGIC!")

#Exemple 3. Simple function call divide()
def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("don't divide by zero please!")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

print(divide(1,2))
print(divide(1,"a"))

# Community SOLUTIONS 3.3.1
def divide(a,b):
    try:
        result = a/b
    except TypeError as t:
            print(f'\nOnly divide ints please: {t}')
    except ZeroDivisionError as z:
            print(f'\nDon\'t divide by zero please: {z}')
    else:
        print(f'\n{a} divided by {b} is {result}')

divide(1,2)
divide(1,"a")
divide(1,0)

# Community SOLUTIONS 3.3.2
def divide(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as err:
        if str(err) == "division by zero":
            print("don't divide by zero please!")
        elif str(err) == "unsupported operand type(s) for /: 'int' and 'str'":
            print("a and b must be ints or floats")
    else:
        print(f"{a} divided by {b} is {result}")


divide(1, 2)
divide(1, "a")
divide(1, 0)

# Community SOLUTIONS 3.3.3
def divide(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as err:
        if err.__class__ == ZeroDivisionError:
            print("don't divide by zero please!")
        elif err.__class__ == TypeError:
            print("a and b must be ints or floats")
    else:
        print(f"{a} divided by {b} is {result}")


divide(1, 2)
divide(1, "a")
divide(1, 0)

#Exemple 3.2. Another version 1
def divide(a,b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong!")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

#print(divide(1,2))
print(divide(1,"a"))

#Exemple 3.3. Another version 2 (Doesn'work well)
def divide(a,b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        if ZeroDivisionError:
            print("don't divide by zero please!")
        elif TypeError:
            print("a and b must be ints or floats")
            print(err)
    else:
        print(f"{a} divided by {b} is {result}")

print(divide(1,2))
print(divide(1,"a"))
print(divide(1,0))

'''
Debugging with PDB
'''
import pdb
first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)

# import pdb;
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)
# q (to quite the debugging mode)

''' PDB Gotcha '''
def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace()

    return a + b + c + d

# There is a conflic with te variable names, to solved you
# can do this:  p c .... p stand for print

print("------------ My solution. Debugging and Errors Exercise 72 --------------------")
# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct amount of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

    # Examples

    # divide(4,2)  2
    # divide([],"1")  "Please provide two integers or floats"
    # divide(1,0)  "Please do not divide by zero"

#Exemple 3. Simple function call divide()
def divide(num1,num2):
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("don't divide by zero please!")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        return result

print(divide(1,2))
print(divide(1,"a"))
