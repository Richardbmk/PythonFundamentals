print("------- My solution 1 ----------")

def generate_evens():
    r = list(range(1,50))
    evens = [num for num in r if num % 2 == 0]
    return evens

print(generate_evens())

print("------- COLT SOLUTION 1 ----------")

def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]

print("------- COLT SOLUTION 2 ----------")

def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result
