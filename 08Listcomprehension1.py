# Activities
print("---------------- My Solution -------------")

folks = ["Elie", "Tim", "Matt"]
answer = [folk[0] for folk in folks]

numbers = [1, 2, 3, 4, 5, 6]
answer2 = [num for num in numbers if num%2 == 0]

print("---------------- COLT SOLUTION 1 -------------")
answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]




print("---------------- COLT SOLUTION 2 -------------")

answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])

answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)
