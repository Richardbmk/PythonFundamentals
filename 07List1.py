print("---------My solution------------------")

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

for i in range(0,len(sounds)):
    list_upper = sounds[i].upper()
    result = print(list_upper, end="")
    result
    
print("")
print("---------COLT SOLUTION 1------------------")
result = ""
for s in sounds:
    result += s.upper()
    print(result)


print("---------COLT SOLUTION 2------------------")
result = ""
for s in sounds:
    result += s
result = result.upper()
print(result)

print("---------ZARKO SOLUTION 1------------------")
# Define your code below:
result = ""

for i in range(0,len(sounds)):
    list_upper = sounds[i].upper()
    result += list_upper
print(result)
