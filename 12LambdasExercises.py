'''
Here we are going to put all the exercises about Lambdas
'''

print("------------ My solution. Lambda Exercise 61 --------------------")

cube = lambda x: x*x*x

print(cube(2)) # 8


print("------------ COLT SOLUTION. Lambda Exercise 61 --------------------")
cube = lambda num: num ** 3

print("------------ My solution. Lambda Exercise 62 --------------------")

def decrement_list(list_numbers):
    return list(map(lambda x: x-1, list_numbers))

#decrement_list = list(map(lambda x: x-1, list_numbers))

print(decrement_list([1,2,3]))
print(decrement_list([20, 14, 11]))


print("------------ My solution. Lambda Exercise 63 --------------------")

def remove_negatives(list_numbers):
    return list(filter(lambda x: not x < 0, list_numbers))

print(remove_negatives([-1, 3, 4, -99, 0]))

print("------------ COLT SOLUTION. Lambda Exercise 63 --------------------")
def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))

print("------------ My solution. Lambda Exercise 64 --------------------")

def is_all_strings(only_string):
    return all([type(name) == str for name in only_string])


print(is_all_strings([1,2,3]))
#print(is_all_strings(["a", "b", "c"]))


print("------------ COLT SOLUTION 1. Lambda Exercise 64 --------------------")

def is_all_strings(lst):
    return all(type(l) == str for l in lst)


print("------------ COLT SOLUTION 2. Lambda Exercise 64 --------------------")

def is_all_strings(lst):
    return all([type(l) == str for l in lst])

print("------------ My solution. Lambda Exercise 65 --------------------")

def extremes(iterable):
    return (min(iterable), max(iterable))

print(extremes([1, 2, 3, 4, 5]))
print(extremes([99, 25, 30, -7]))
print(extremes(["alcatraz"]))

print("------------ My solution. Lambda Exercise 66 --------------------")

def max_magnitude(single_list):
    return max([abs(num) for num in single_list])

print(max_magnitude([300, 20, -900]))

print("------------ COLT SOLUTION. Lambda Exercise 66 --------------------")
def max_magnitude(nums):
    return max(abs(num) for num in nums)

print("------------ My solution 1. Lambda Exercise 67 --------------------")

def sum_even_values(single_list):
    return sum([num for num in single_list if num % 2 == 0])


print(sum_even_values([1,2,3,4,5,6]))

print("------------ My solution 2. Lambda Exercise 67 --------------------")

def sum_even_values(*args):
    return sum(num for num in args if num % 2 == 0)

print(sum_even_values(1,2,3,4,5,6))

print("------------ My solution 3. Lambda Exercise 67 --------------------")

def sum_even_values(*args):
    total = 0
    for num in args:
        if num % 2 == 0:
            total += num
    return total

print(sum_even_values(1,2,3,4,5,6))

print("------------ COLT SOLUTION. Lambda Exercise 67 --------------------")

def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)


print("------------ My solution. Lambda Exercise 68 --------------------")

def sum_floats(*args):
    return sum(num for num in args if isinstance(num, float))

print(sum_floats(1.5, 2.4, 'awesome', [], 1))


#[num for num in args if isinstance(num, float)]
#args = [1.5, 2.4, 'awesome', [], 1]

print("------------ COLT SOLUTION. Lambda Exercise 68 --------------------")

def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)

print(sum_floats(1.5, 2.4, 'awesome', [], 1))



print("------------  My solution. Lambda Exercise 69 --------------------")

def interleave(string1, string2):
    scoby = list(zip(string1, string2))
    scoby2 = list(scoby[0]) + list(scoby[1]) + list(scoby[2])
    return "".join(scoby2)

print( interleave("aaa", "zzz"))

print("------------ COLT SOLUTION. Lambda Exercise 68 --------------------")

def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))

print("------------  My solution. Lambda Exercise 70 --------------------")

def triple_and_filter(list):
    return [num*3 for num in list if num % 4 == 0]

print(triple_and_filter([6,8,10,12]))

print("------------ COLT SOLUTION. Lambda Exercise 70 --------------------")

def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

print("------------  COLT SOLUTION. Lambda Exercise 71 --------------------")

def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']
