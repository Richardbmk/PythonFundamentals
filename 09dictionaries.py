# Dictionaries in python
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

cat = {"name": "blue", "age": 3.5, "isCute": True}

# A combination of a list and Dictionaries
cart = [{"name": "blue", "age": 3.5, "isCute": True}]

# Dict
cat2 = dict(name = "Richard")
cat2 = dict(name = "Richard", age="5")

# Accessing Individual Values

instructor["name"]  #"Colt"
instructor["owns_dog"] #True

# Acces all values in a Dictionaries
instructor.values()

for v in instructor.values():
    print(v)

# Acces all keys in a Dictionaries
instructor.keys()

for v in instructor.keys():
    print(v)

# Acces all keys and values in a Dictionaries
instructor.items()

for k,v in instructor.items():
    print(f"key is {k} and value is {v}")

# Does a dictionary have a key?
"name" in instructor # True
"awesome" in instructor # False

# Does a dictionary have a value?
"Colt" in instructor.values() # True
"Nope!" in instructor.values() # False

# Dictionary Mecthods

# Method clear
d = dict(a=1,b=2,c=3)
d.clear()
d # {}

#Method copy
d = dict(a=1,b=2,c=3)
c = d.copy()
c # {'a': 1, 'b': 2, 'c': 3}
c is d # False
c == d # True

# Method fromkeys

{}.fromkeys("a","b") # {'a': 'b'}
{}.fromkeys(["email"], 'unknown') # {'email': 'unknown'}
{}.fromkeys("a",[1,2,3,4,5]) # {'a': [1, 2, 3, 4, 5]}
{}.fromkeys("phone", "unknown") # {'p': 'unknown', 'h': 'unknown', 'o': 'unknown', 'n': 'unknown', 'e': 'unknown'}
new_user = {}.fromkeys([])
new_user.fromkeys(range(1,10), "unknown")

# Method Get
d = dict(a=1,b=2,c=3)
d['a'] # 1
d.get('a') # 1
d['b'] # 2
d.get('b') # 2
d['no_key'] # KeyError
d.get('no_key') # None

# Method pop:

d = dict(a=1,b=2,c=3)
d.pop() # TypeError: pop expected at least 1 arguments, got 0
d.pop('a') # 1
d # {'c': 3, 'b': 2}
d.pop('e') # KeyError

# Method popitem()

d = dict(a=1,b=2,c=3,d=4,e=5)
d.popitem() # ('d', 4)
d.popitem('a') # TypeError: popitem() takes no arguments (1 given)

#Method update
instructor
person = {"City": "Antigua"}
person.update(instructor)

person["name"] = "Evelia"
person.update(instructor)

# Dictionary Comprehension

# {__:__for__in__}
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key,value in numbers.items()}
print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}

{num: num**2 for num in [1,2,3,4,5]}

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))}
print(combo) # # {'A': '1', 'B': '2', 'C': '3'}

instructor
yelling_instructor = {k.upper(): v.upper() for k,v in instructor.items()}
yelling_instructor = {(k.upper() if k is "color" else k): v.upper() for k,v in instructor.items()}


# Conditional logic of Dictionary Comprehension
num_list = [1,2,3,4]

{ num:("even" if num % 2 == 0 else "odd") for num in num_list }
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

{ num:("even" if num % 2 == 0 else "odd") for num in range(1,100) }
