"""
Exercise 25
From the following text:



string = '1 0 0 1 0 1'


remove spaces using slicing. Then convert the result to decimal notation and print to the console as shown below.ole.
"""

# My solution
string = '1 0 0 1 0 1'
string_1 = "".join(string.split(" "))
string_decimal = int(string_1, 2)
print(f"Number found: {string_decimal}")

# Others solution
string = '1 0 0 1 0 1'
binary = string[::2]
number = int(binary, 2)
print(f'Number found: {number}')