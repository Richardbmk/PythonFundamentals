# Exercise 39
print("------- My solution ----------")
def generate_evens():
    return [x for x in range(50) if x%2 == 0]


def generate_evens1():
    list = []
    for n in range(50):
        if(n % 2 == 0):
            list.append(n)
    return list 
print("------- COLT SOLUTION 1 ----------")

def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]


print("------- COLT SOLUTION 2 ----------")
def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result


# Exercise 40
def yell(letter):
    return letter.upper()

# Exercise 41
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count 

 count_dollar_signs("$super S$ize")

# Exercise 42
print("------- My solution ----------")
def speak(animal):
    animalSounds = {
       "pig" : "oink",
       "duck": "quack",
       "cat" : "meow",
       "dog" : "woof", 
    }
    if (animal in animalSounds.keys()):
        return animalSounds[animal]
    else:
        return "?"



animalSounds = {
    "pig" : "oink",
    "duck": "quack",
    "cat" : "meow",
    "dog" : "woof", 
}

animalSounds["pig"]

speak("duck")

speak("bruja")
print("------- COLT SOLUTION 1 ----------")
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
         return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

print("------- COLT SOLUTION 2 ----------")
def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"




# Exercise 43
print("------- My solution ----------")

def product(a, b):
    return a*b

#print(product(6, 6))

print("------- COLT SOLUTION 1 ----------")

def product(a,b):
    return a*b

# Exercise 44
print("------- My solution ----------")
def return_day(day):
        days = {1 :'Sunday', 2 :'Monday', 3 :'Tuesday', 4 :'Wednesday', 5 : 'Thursday', 6 : 'Friday', 7 : 'Saturday'}
        return days.get(day)


def return_day(num):
    dayWeeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    try:
        return dayWeeks[num-1]
    except:
        return "None"

#print(return_day(9))

print("------- COLT SOLUTION 1 ----------")

def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0
        return days[num-1]
    return None

print("------- COLT SOLUTION 2 ----------")

def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

# Exercise 45

print("------- My solution ----------")

def last_element(lists):
            return lists[len(lists)-1]

#print(last_element([1, 2, 3, 4, 5, 6, 7]))


print("------- COLT SOLUTION 1 ----------")

def last_element(l):
    if l:
        return l[-1]
    return None


# Exercise 46
print("------- My solution ----------")
def number_compare(a, b):
    if a > b:
        return "first is greater"
    elif b > a:
        return "Second is greater"
    else:
        return "Numbers are equal"

#print(number_compare(1, 1))

print("------- COLT SOLUTION 1 ----------")
def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"

# Exercise 47
print("------- finded solution 47 ----------")
'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

def single_letter_count(word, letter):
    if letter in word.lower():
        return word.lower().count(letter.lower())
    else:
        return 0

#print(single_letter_count("Flow state", "y"))

print("------- COLT SOLUTION 47 ----------")

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())

print("------- My solution 48 ----------")
'''
you're returning a dictionary but the value in that dictionary, for any
particular character, is the position of that character in the string, +1,
not the number of times it appears.
'''
def multiple_letter_count(string):
    list_word = list(string)
    count_letters = count(list_word)
    return {string[i]: i+1 for i in range(0, len(string))}

#print(multiple_letter_count("awesome"))

#Solving the real proble3m
def multiple_letter_count(string):
    return {string[i]: string.count(string[i]) for i in range(0, len(string))}

#print(multiple_letter_count("awesome"))

print("------- COLT SOLUTION 48 ----------")
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}
---------------------------------------------------------------------------
print("------- My Solution 49 ----------")

'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list, command, location, value=1):
    if command == "remove" and location == "end":
        last_value = list.pop()
        return last_value
    elif command == "remove" and location == "beginning":
        first_value = list.pop(0)
        return first_value
    elif command == "add" and location == "beginning":
        add_value = list.insert(0, value)
        return list
    elif command == "add" and location == "end":
        add_value = list.insert(len(list), value)
        return list

#print(list_manipulation([1,2,3], "remove", "end")) # 3
#print(list_manipulation([1,2,3], "remove", "beginning")) #  1
#print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
#print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]

print("------- COLT SOLUTION 49 ----------")

def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

print("------- My Solution 50 ----------")
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(anything):
    anything = anything[::-1]
    #print(backward)
    anything = anything.lower()
    #print(case_sensitive)
    anything= anything.replace(" ", "")
    #print(join_anything)
    #print(type(join_anything))
    if anything == anything:
        return True
    else:
        return False

print(is_palindrome("deg ged")) # True

print("------- COLT SOLUTION(1) 50 ----------")

def is_palindrome(string):
    return string == string[::-1]

print("------- COLT SOLUTION(2) 50 ----------")

def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]


print("------- My Solution 51 ----------")
'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''
def frequency(list, value):
    frequence = list.count(value)
    return frequence

def frequency(list, value):
    return list.count(value)


print(frequency([1,2,3,4,4,4], 4)) # 3

print("------- COLT SOLUTION 51 ----------")

def frequency(collection, searchTerm):
    return collection.count(searchTerm)

print("------- My Solution 52 ----------")

'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''
def multiply_even_numbers(list):
    evens_list = [num for num in list if num % 2 == 0]
    product = 1
    for i in evens_list:
        product *= i
    return product
print(multiply_even_numbers([2,4,6])) # 48


print("------- COLT SOLUTION 52 ----------")

def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total


print("------- My Solution 53 ----------")

'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''
def capitalize(name):
    return name[0].upper()+name[1:]

print(capitalize("tim")) # "Tim"

print("------- My Solution 53 ----------")

def capitalize(string):
    return string[:1].upper() + string[1:]


print("------- My Solution 54 ----------")
'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''
def compact(truthy_values):
    return [num for num in truthy_values if num]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))

print("------- COLT SOLUTION(1) 54 ----------")

def compact(l):
    return [val for val in l if val]

print("------- COLT SOLUTION(1) 54 ----------")

def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals

print("------- My solution (1) 55 ----------")

def intersection(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    list_convert = list(list1 & list2)
    return list_convert

def intersection(list1, list2):
    return list(set(list1) & set(list2))
    
print(intersection([1,2,3], [2,3,4]))

print("------- My solution (2) 55 ----------")

def intersection(list1, list2):
    return list(set(list1) & set(list2))

print(intersection([1,2,3], [2,3,4]))


print("------- COLT SOLUTION 55 ----------")

def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common

print("------- My solution 56 ----------")
'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def isEven(list):
    return [num for num in list if num % 2 == 0]

def partition(list, fn=isEven):
    list2 = [num for num in list if num % 2 != 0]
    return [isEven(list), list2]

print(partition([1,2,3,4], isEven)) #[[2, 4], [1, 3]]

print("------- COLT SOLUTION (1) 56 ----------")

def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

print("------- COLT SOLUTION (2) 56 ----------")

def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]
