my_stuff = ["books", "11.5", "love", "sex"]

nums = list(range(1,100))

friends = ["Sam","laia", "Laura", "Johan"]
# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

#Change "Hanna" to "Hannah"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[-2] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
people[-1] = "Aparna"

for homie in friends:
    print(homie)

index = 0
while index < len(friends):
    print(friends[index])
    index += 1

index = 0
while index < len(friends):
    print(f"{index}: {friends[index]}")
    index += 1

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

for i in range(0,len(sounds)):
    result = sounds[i].upper
    print(result, end="")
