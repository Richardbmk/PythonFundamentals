""" 
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
"""
def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

# EXPLANATION EXPLANATION EXPLANATION EXPLANATION

[s[0].upper() + s[1:] for s in "hola ricardo el grande".split()]
# Python program to demonstrate the 
# use of join function to join list 
# elements with a character. 
  
list1 = ['1','2','3','4']  
  
s = "-"
  
# joins elements of list1 by '-' 
# and stores in sting s 
s = s.join(list1) 
  
# join use to join a list of 
# strings to a separator s 
print(s) 

'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''
def find_factors(num):
    vector = []
    i = 1
    while (i <= num):
        if num % i == 0:
            vector.append(i)
        i += 1
    return vector


'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''
def includes(item,val,start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]

# EXPLANATION EXPLANATION EXPLANATION EXPLANATION
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}
"Python" in instructor.values() # True
"name" in instructor.keys() # True

val in item # Comprueba la información que hay y devuelve True o Flase. Solo para listas y strings
val in item[start:] # Evalua desde el valor start para delante!


'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''
## This solution is not accepted!
def repeat(gt, num):
    print(str(gt)*num)

## New solution
def repeat(string, num):
    if (num == 0):
        return ''
    i = 0
    newString = ''
    while (i < num):
        newString += string
        i += 1
    return newString

'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''

def truncate(string, n):
    if (n < 3):
        return "Truncation must be at least 3 characters."
    if (n > len(string) + 2): # I don't understant this apart at all 
        return string
    return string[:n - 3] + "..."