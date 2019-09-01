#Exercise
print("-------- My Solution -----------")
artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist["first"] + " " + artist["last"]
print(full_name)

print("-------- COLT SOLUTION 1 -----------")

artist = {
    "first": "Neil",
    "last": "Young",
}
# concat first and last name with a space
full_name = artist["first"] + " " + artist["last"]
print(full_name)

print("-------- COLT SOLUTION 2 -----------")

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = "{} {}".format(artist["first"],artist["last"])
print(full_name)

print("-------- COLT SOLUTION 3 -----------")

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"
print(full_name)
