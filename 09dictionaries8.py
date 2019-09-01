#Exercise
print("-------- My Solution -----------")

answer = {}.fromkeys("aeiou", 0)
print(answer)

print("-------- COLT SOLUTION 1 -----------")
answer = {char:0 for char in 'aeiou'}

print("-------- COLT SOLUTION 2 -----------")
answer = dict.fromkeys("aeiou", 0)
