""" 
reverse_string:

Write a function called reverse_string which accepts
a string and return a new stirng with all the characters
reversed. 

"""
# Solution 1

def reverse_string(words):
    return [word[::-1].lower() for word in words]

print(reverse_string(["hola"]))



# Solution 2 (BEST SOLUTION 1)
def reverse_string(word):
    return word[::-1]

print(reverse_string("Ricard"))
"Hola"[1::2]



# Solution 3 (BEST SOLUTION 2)
def reverse_string(word):
    return ''.join(reversed(word))

reverse_string("Richard")


''.join(reversed("Richard"))

# Colt Solution
