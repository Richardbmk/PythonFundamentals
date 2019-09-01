# Activities
print("---------------- My Solution 1 -------------")

bla = [char for char in "amazing" if char not in "aeiou"]
print(bla)


print("---------------- COLT SOLUTION 1 -------------")

answer = [char for char in "amazing" if char not in "aeiou"]
print(answer)

print("---------------- COLT SOLUTION 2 -------------")

answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]]
print(answer)
