# 262 Special_magic_methods
from copy import copy
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "CANT MULTIPLY!"

j = Human("Jennifer", "Larson", 59)
k = Human("Sinatra", "Ventura", 39)

# print(j)
# print(len(j))
# print(j + k)
# print(j * 2)

# triplets = j * 3
# triplets[1].first = "Jessica"
# print(triplets)
# print((j + k) * 3)


# 263. Making a Grumpy Dictionary - Overriding Dict
class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AINT HERE!")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK FINE...")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("NO IT AINT IN HERE")
        return False


d = GrumpyDict({"name": "Yolo", "City": "New York"})
# print(d)
# d["mad"]
# d["City"] = "Barcelona"
# print(d)
# "Flow" in d

# Exercise Special Methods Train
class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        # Python 2.x notation
        # return "{} car train".format(self.num_cars)
        return f"{self.num_cars} car train"

    def __len__(self):
        return self.num_cars

a_train = Train(4)
print(a_train)
print(len(a_train))
