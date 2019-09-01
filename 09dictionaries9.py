#Exercise
print("-------- My Solution 1 -----------")

answer = {f"chr({num})":chr(num) for num in range(65,91)}
print(answer)

print("-------- My Solution 2 -----------")

answer = {"chr({})".format(num):chr(num) for num in range(65,91)}
print(answer)

print("-------- My Solution 3 -----------")

answer = {num:chr(num) for num in range(65,91)}
print(answer)

print("-------- COLT SOLUTION 1 -----------")
answer = {count: chr(count) for count in range(65,91)}
