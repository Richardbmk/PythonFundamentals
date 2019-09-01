# 256. Inheritance Example. User and Moderator
# Class Methos. 245
class User:
    active_users = 0

    @classmethod
    def display_active_user(cls):
        return f"There are currently {cls.active_users} active_users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age=0):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"
    def __repr__(self):
        return f"{self.first} is {self.age}"

class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active mods"

    def remove_post(self):
        return f"{self.full_name} removed a post from the {self.community} community"

# jasmine = Moderator("Jasmine", "O'conner", 61, "Piano")
# print(jasmine.full_name())
# print(jasmine.community)

# print(User.display_active_user())
# u1 = User("Richard", "Nano", 35)
# print(User.display_active_user())
# jasmine = Moderator("Jasmine", "O'conner", 61, "Piano")
# print(User.display_active_user())

# u1 = User("Richard", "Nano", 35)
# u2 = User("Richard", "Nano", 35)
# u3 = User("Richard", "Nano", 35)
# jasmine = Moderator("Jasmine", "O'conner", 61, "Piano")
# jasmine = Moderator("Jasmine", "O'conner", 61, "Piano")
# print(User.display_active_user())
# print(Moderator.display_active_mods())

'''
Roleplaying Game Classes
'''
# My solu
class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    @classmethod
    def speak(cls):
        return f"I heard something there"


village = NPC("bOB", 100, 12)
print(village.name)
print(village.hp)
print(village.level)
print(village.speak())

# Colt Solution
class Character():
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return "{0} says: 'I heard monsters running around last night!'".format(self.name)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#258 The Crazy word of Multiple Inheritance
class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"

class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        super().__init__(name=name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#259 The Crazy word of Multiple Inheritance
class A:
    def do_somthing(self):
        print("Method Defined In: A")
class B(A):
    def do_somthing(self):
        print("Method Defined In: B")

class C(A):
    def do_somthing(self):
        print("Method Defined In: C")

class D(B, C):
    pass
    # def do_somthing(self):
    #     print("Method Defined In: D")

# thing = D()
# print(thing.do_somthing())

print(D.__mro__)
print(D.mro())
help(D)

# EXERCISE MRO GENETICS

class Mother():
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type

class Father():
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type

class Child(Mother, Father):
    pass
