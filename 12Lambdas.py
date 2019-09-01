'''
Lambdas
'''
squere2 = lambda num: num * num

add = lambda a,b: a + b

print(squere2(7))
print(add(3,9))

print(squere2.__name__)
print(add.__name__)

# More exemple

first_lambda = lambda x: x + 5

first_lambda(10) # 15

first_lambda.__name__ # '<lambda>'

# More exemple
add_values = lambda x, y: x + y
multiply_values = lambda x, y: x * y

add_values(10, 20) # 30
multiply_values(10, 20) # 200

'''
Built in functions with lambdas
map
'''
nums = [2, 3, 4, 5, 6]

doubles = map(lambda x: x*2, nums)
doubles
for num in doubles:
    print(num)

list(doubles)
doubles = list(map(lambda x: x*2, nums))

people = ["Darcy", "Christina", "Dana", "Annabel"]

peeps = map(lambda name: name.upper(), people)
list(peeps)


# ANother exemple
names = [
    {'first':'Rusty', 'last': 'Steele'},
    {'first':'Colt', 'last': 'Steele', },
    {'first':'Blue', 'last': 'Steele', }
]

first_names = list(map(lambda x: x['first'], names))

first_names # ['Rusty', 'Colt', 'Blue']

# Using with functions
def double(x):
    return x*2

double(3)

doubles = list(map(double, nums))

'''
Built in functions with lambdas
filter
'''
l = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, l))

evens # [2,4]

names = ["Darcy", "Christina", "Dana", "Annabel"]
names
d_names = filter(lambda n: n[0]=="D", names)
d_names
list(d_names)

# Big exemple
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

inactive_users = list(filter(lambda u: len(u["tweets"]) == 0, users))
print(inactive_users)
inactive_users = list(filter(lambda u: ["tweets"]), users)) # You will obtain de opposite

#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))


#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(),
	filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]



# MOre Exemples
names = ['Lassie', 'Colt', 'Rusty']

list(map(lambda name: f"Your instructor is {name}",
     filter(lambda value: len(value) < 5, names)))

# ['Your instructor is Colt']

# Example using List comprehension

names = ['Lassie', 'Colt', 'Rusty']

[f"Your instructor is {name}" for name in names if len(name) < 5]

'''
Built in functions
'''
# Method all
all([0, 1, 2, 3]) # False

all([char for char in "eio" if char in "aeiou"])
[char for char in "eio" if char in "aeiou"]

all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]) #True
[num for num in [4, 2, 10, 6, 8] if num % 2 == 0]

people = ["Charle", "Casey", "Cody", "Carly", "Cristina"]
all([name[0]=="C" for name in people])
[name[0]=="C" for name in people]
people.append("Kristy")
[name[0]=="C" for name in people]
all([name[0]=="C" for name in people])

#Method Any
any([0, 1, 2, 3]) #True
any([val for val in [1,2,3] if val > 2]) #True
any([val for val in [1,2,3] if val > 5]) #False

nums = [2, 60, 26, 18, 21]
any([num % 2 == 0 for num in nums])
any([num % 2 == 1 for num in nums])
any([num % 2 != 0 for num in nums])

#Generator Expressions and Using sys.getsiceof
(char for char in "eio" if char in "aeiou") # (char for char in "eio" if char in "aeiou")

 # Code to prove the utility of Generator Expression
import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))
print("Todo the same thing, it takes...")
print(f"List comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")

# Method sorted

# sorted (works on anything that is iterable)

more_numbers = [6,1,8,2]
sorted(more_numbers) # [1, 2, 6, 8]
print(more_numbers) # [6, 1, 8, 2]

nums = [4, 5, 1, 55, 22, 34]
nums.sort()

nums = [4, 5, 1, 55, 22, 34]
sorted(nums)
nums
sorted(nums, reverse=True)
nums

sorted((2, 1, 4, 33, 22, 90))

# Another exemple
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

sorted(users, key=len) # Ordered by the lenth of the dictionari
sorted(users, key=lambda user: user["username"])
sorted(users, key=lambda user: len(user["tweets"]))


#Another Exemples with my fovirite songs

songs = [
        {"title": "Heard 'Em Say'", "artists": ["Kaney West", "Adam Levine"], "duration": 3.23},
        {"title": "Just Give Me a Reason", "artists": ["P!ink", "Nate Ruess"], "duration": 4.02},
        {"title": "HeadLights", "artists": ["Eminem", "Nate Ruess"], "duration": 5.43},
        {"title": "Rose Golden", "artists": ["Kid Cudi", "Willow"], "duration": 4.37}
]

sorted(songs, key=lambda s: s["duration"])
sorted(songs, key=lambda s: s["duration"], reverse=True)

'''
Reduce Built functions
'''
from functools import reduce

l = [1,2,3,4]

product = reduce(lambda x, y: x * y, l)

l = [1,2,3,4]

total = reduce(lambda x, y: x + y, l, 10)

'''
Min and Max Built functions
'''
max(3, 67, 99)

max("a", "b", "c")

nums = [30, 32, 5, 6, 90]
min(nums)
max(nums)

max("hello word")

min("hello word")

max((3, 4, 34, 55))

names = ["Arya", "Samson", "DOra", "Tim", "Ollivander"]
min(names)
max(names)

min(len(names) for names in names) # 3

(len(names) for names in names) # (len(names) for names in names)

[len(names) for names in names] # [4, 6, 4, 3, 10]


max(names, key=lambda n:len(n)) # "Ollivander"

min(names, key=lambda n:len(n))  # "Tim"

songs = [
        {"title": "Heard 'Em Say'", "artists": ["Kaney West", "Adam Levine"], "duration": 3.23},
        {"title": "Just Give Me a Reason", "artists": ["P!ink", "Nate Ruess"], "duration": 4.02},
        {"title": "HeadLights", "artists": ["Eminem", "Nate Ruess"], "duration": 5.43},
        {"title": "Rose Golden", "artists": ["Kid Cudi", "Willow"], "duration": 4.37}
]

min(songs, key=lambda s: s["duration"])
max(songs, key=lambda s: s["duration"])
max(songs, key=lambda s: s["duration"])["title"]

max = 0
for song in songs:
    if song["artists"] > max
        max = song["duration"]

'''
reversed Built in functions
'''
nums = [1, 2, 3, 4]
nums.reverse()
nums

reversed(nums)
list(reversed(nums))

reversed("hello")

for char in reversed("hello word"):
    print(char)

"hello"[::-1]


reversed("hello")
list(reversed("hello"))
"".join(list(reversed("hello")))

for x in reversed(range(0,10)):
    print(x)


'''
Len() and Special Sneak Peak of OPP!
'''
len("asdasdas")

len({"s": 10, "10": "as"})

len({})

class SpecialList:

    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return self.__data.__len__() // 2

l1 = SpecialList([1, 40, 40, 20])
l2 = SpecialList([1, 40, 40, 20])

print(len(l1))
print(len(l2))

'''
Built in Fuctions
abs(), Sum() and Round()
'''
# Abs
abs(-23)

abs(float("20"))

import math
math.fabs(-4)

# sum

sum([1, 2, 3])

sum([1, 2, 3], 10)

sum([1, 2, 3], -6)

sum((1.5, 2, 3.7))

sum({1,50,10})
"".join(["hi", "there"])

# Roand

round(3.91834324)

round(3.91834324, 2)

round(3.91834324, None)

'''
Built in functions
zip
'''
first_zip = zip([1, 2, 3], [4, 5, 6])
flist(first_zip)
dict(first_zip)

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

zip(nums1, nums2)

z = zip(nums1, nums2) #[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
list(z)
dict(z)

z = zip(nums2, nums1) #[(6, 1), (7, 2), (8, 3), (9, 4), (10, 5)]

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10, 11]
zip(nums2, nums1) #[(6, 1), (7, 2), (8, 3), (9, 4), (10, 5)]

words = ["hi", "lol", "haha", ":-)", "Richard"]
list(zip(words, nums1, nums2)) #[('hi', 1, 6), ('lol', 2, 7), ('haha', 3, 8), (':-)', 4, 9), ('Richard', 5, 10)]

five_by_two = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
list(zip(*five_by_two)) #[(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)]

# More exemples about zip

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["dan", "ang", "kate"]

# final_grades = {"dan": 98, "ang": 91, "kate": 78}

final_grades = [pair for pair in zip(midterms, finals)]

final_grades = [max(pair) for pair in zip(midterms, finals)]

final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}

print(final_grades)

    # Another way of doing the same

scores = map(
    lambda pair: max(pair)
    zip(midterms, finals)
)
print(list(scores))
    # Another way of doing the same
grades = zip(
            students,
            map(
                lambda pair: max(pair),
                zip(midterms, finals)
            )
)

print(dict(grades))
    # Another way of doing the same
final_grades = dict(
    zip(
                students,
                map(
                    lambda pair: max(pair),
                    zip(midterms, finals)
                )
    )
)

print(final_grades)


    # Another way of doing the same
avg_grades = dict(
    zip(
                students,
                map(
                    lambda pair: ((pair[0]+pair[1])/2),
                    zip(midterms, finals)
                )
    )
)

print(avg_grades)
