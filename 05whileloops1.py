print("------- My solution -----------")
emogi = input("wich tipe of figure you like? ")
num = 0
for let in emogi:
    while num < 9:
        num += 1
        print(let*num)

print("------- COLT SOLUTION 1 -----------")

for num in range(1,11):
    print("\U0001f600" * num)

print("------- COLT SOLUTION 2 -----------")

times = 1
while times < 11:
    print("\U0001f600" * times)
    times += 1

print("------- COLT SOLUTION 3 -----------")

#Nested loops, is repeaten something that i repeaten on his own
for x in range(3):
    for num in range(1,11):
        print("\U0001f600" * num)

print("------- COLT SOLUTION 4 -----------")
# Without string multiplicationi - ugly solution
for num in range(1,11):
    count = 1
    smileys = ""
    while count <= num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)
