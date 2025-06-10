"""
Exercise 24
From the following text:



string = 'PKV-89415-PLN'


extract the code containing the first three and last three characters. Print the result to the console.
"""

# My solution
string = 'PKV-89415-PLN'
string_list = string.split("-")
result = string_list[0] + string_list[2]
print(result)

# Others solution
string = 'PKV-89415-PLN'
code = string[:3] + string[-3:]
print(code)