'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''
def sum_up_diagonals(arr):
    total = 0
    
    for i,val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1-i]
    return total



'''
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''

def min_max_key_in_dictionary(dics):
    suit = [(k, v) for k,v in dics.items()]
    return [min(suit)[0], max(suit)[0]]

# COLT SOLUTION
def min_max_key_in_dictionary(d):
    keys = d.keys()
    return [min(keys), max(keys)]


### FINDING THE SOLUTION!
stats = {'a':1000, 'b':3000, 'c': 100}

inverse = [(value, key) for key, value in stats.items()]

print(max(inverse)[1])


suit = {2:'a', 7:'b', 1:'c',10:'d',4:'e'}






'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j+=1
        j = i+1
        i+=1
    return count;





'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''

def two_oldest_ages(tie):
    return sorted(tie)[-2:]

# EXPLANATION
lot[-2:]


lot = [1, 2, 10, 8]

lot.sort()

lot # [1, 2, 8, 10]





'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''

def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1



total = 10 

total = 10 or 0 

total % 2 == 1

total % 0 == 1