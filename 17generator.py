# 270. Introduction to Generators

# Generators function

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# print(count_up_to(5))

counter = count_up_to(5)
# counter
# print(next(counter))
# print(list(counter))

for num in counter:
    print(num)

# Veek Generator EXERCISE
# print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# Colt solution
def week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        yield day

weeks = week()


for puf in weeks:
    print(puf)

print(list(weeks))

# yes_or_no EXERCISE (Colt Solution)

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"


# 273. Writing a Beat Making Generator

# Bad version
def current_beat():
    max = 100
    nums = (1,2,3,4)
    i = 0
    result = []
    while len(result) < max:
        if i >= len(nums): i = 0
        result.append(nums[i])
        i += 1
    return result

# print(current_beat())

# Improved version

def current_beats():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1

nuture = current_beats()
print(next(nuture))

# make a son EXERCIE

def make_song(count=99, beverage="soda"):
    i = 0
    while i < count:
        yield f"{i} bottles of {beverage} on the wall."
        i += 1

# Colt solution
def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield f"{num} bottles of {beverage} on the wall."
        elif num == 1:
            yield f"Only 1 bottle of {beverage} left!"
        else:
            yield "No more {beverage}!"

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# 275. Testing Memory Usage With Generators
def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

# print(fib_list(10))

def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count += 1

for n in fib_list(10):
    print(n)

# Exercise Get Multiple Generator COLT SOLUTION

def get_multiples(num=1, count=10):
    nex_num = num
    while count > 0:
        yield nex_num
        count -= 1
        nex_num += num

evens = get_multiples(2, 3)

# Exercise Unlimited Multiples COLT SOLUTION

def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        nex_num += num

# Generator Expressions

def nums():
    for num in range(1,10):
        yield num

g = nums()
next(g)

# All in one line
t = (num for num in range(1,10))
t # now is come from a generator Expressions
next(t)

l = [num for num in range(1,10)]
l
sum([num for num in range(1,10)]) # List comprenssion
sum(num for num in range(1,10)) # List Expressions

# Example...
import time

gen_start_time = time.time()
print(sum(n for n in range(10000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(10000)]))
list_time = time.time() - list_start_time

print(f"sum(n for n in range(1000)) took: {gen_time}")
print(f"sum([n for n in range(1000)]) took: {list_time}")
