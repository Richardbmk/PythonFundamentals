print("------- My solution 1 ----------")

def yell(uppercase):
    return f"{uppercase.upper()}!"

print(yell("leave me alone"))

print("------- My solution 2 ----------")

def yell(uppercase):
    return "{}!".format(uppercase.upper())

print(yell("i love you"))

print("------- COLT SOLUTION 1 ----------")

def yell(word):
    return word.upper() + "!"

print("------- COLT SOLUTION 2 ----------")

def yell(word):
    return "{}!".format(word.upper())

print("------- COLT SOLUTION 3 ----------")
def yell(word):
    return f"{word.upper()}!"
