print("------- PROBLEM ----------")

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == "$":
            count += 1
    return count

print(count_dollar_signs("fl$ri$da")) #0

print("------- My solution 1 ----------")

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == "$":
            count += 1
    return count

print(count_dollar_signs("fl$ri$da")) #2
