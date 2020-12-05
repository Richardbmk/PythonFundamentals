# Activities
print("---------------- My Solution -------------")

answer = [value for value in [1, 2, 3, 4] if value in [3, 4, 5, 6]]
print(answer)

friends = ["Elie", "Tim", "Matt"]
answer2 = [friend[::-1].lower() for friend in friends]
print(answer2)


## Pruebas
friends = ["Elie", "Tim", "Matt"]
Family = ["Elie", "Juan", "Mattias"]
answer = [value for value in friends if value in Family] # Elie

print("---------------- COLT SOLUTION 1 -------------")

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
print(answer)
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
print(answer2)

print("---------------- COLT SOLUTION 2 -------------")

answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
print(answer)

answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())
print(answer2)
