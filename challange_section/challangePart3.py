'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''
def two_list_dictionary(keys, values):
    colect = {}
    for i,v in enumerate(keys):
        if (i < len(values)):
            colect[keys[i]] = values[i]
        else:
            colect[keys[i]] = None
        
    return colect
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
## EXPLANATION EXPLANATION EXPLANATION
colect = {}
keys = ['a', 'b', 'c', 'd']
val = [1, 2, 3]

colect[keys[1]] = values[1]

print(colect)



'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''

def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end+1])



'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(num1,num2):
    d1 = {letter:str(num1).count(letter) for letter in str(num1)}
    d2 = {letter:str(num2).count(letter) for letter in str(num2)}
  
    for key,val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True
## EXPLANATION EXPLANATION EXPLANATION
num1 = 551122
num2 = 221515
d1 = {letter:str(num1).count(letter) for letter in str(num1)}
d2 = {letter:str(num2).count(letter) for letter in str(num2)}







'''
nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''
def nth(lists, p):
    return lists[p]

nth(['a', 'b', 'c', 'd'], 1)


numw = [1, 2, 5, 9, 8]

numw[-1]

# COLT SOLUTION
def nth(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]

'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''
# My SOLUTION (DOESN'T WORK WELL)
def find_the_duplicate(num):
    d1 = {letter:str(num).count(letter) for letter in str(num)}
  
    for key in d1.keys():
        if d1[key] > 1:
            return key

# COLT SOLUTION
def find_the_duplicate(arr):
    counter = {}
    for val in arr:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)