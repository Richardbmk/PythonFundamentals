#Exercise
print("-------- My Solution -----------")

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {
        "name": "Jared",
        "job": "Musician",
        "city": "Bern"
}

print(answer)

print("-------- COLT SOLUTION 1 -----------")
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}


print("-------- COLT SOLUTION 2 -----------")
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}

print("-------- COLT SOLUTION 3 -----------")
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)
