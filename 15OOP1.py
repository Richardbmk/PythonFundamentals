# # DEFINING THE SIMPLEST POSSIBLE class

class User:
    pass

user1 = User()
print(user1)
print(type(user1))

# Understanting the __init__

class User:
    def __init__(self, first, last, age):
        # print("A NEW USER HAS BEEN MADE!")
        self.first = first
        self.last = last
        self.age = age


user1 = User("Joe", "Smith", 68)
user2 = User("Bianca", "Lubina", 35)
print(user1.first, user1.age)
print(user2.last, user1.first)


# # Exercise about __init__
class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

c = Comment("LUis", "OMG no sabe jugar", 4)
print(c.username, c.text, c.likes)

# 239. Underscors: Dunder Methods, name Mangling,...
class Person:
    def __init__(self):
        self.name = "Ruth"
        self._secret = "hi!"

    #def doorman(self, guess):
    #    if guess == self._secret:
    #        let them in

        self.__msg = "I like turtle!"
        self.__lol = "HAHAHAHAAHHA"

p = Person()

print(p.name)
print(p._secret)
print(dir(p))
print(p._Person__msg)
print(p.__msg) # ain't work!
print(p._Person__lol)

# Another exemple
class User:
    active_users = 0

    def __init__(self, first, last, age):
        # print("A NEW USER HAS BEEN MADE!")
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last} {self.age}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"

    def say_hi():
        print("HELLO!!!")


print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Bianca", "Lubina", 35)

print(user1.full_name())

print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))

print(user1.initials())
print(user2.initials())

print(user2.is_senior())
print(user1.age)
print(user2.birthday())
print(user1.age)


print(User.active_users)
print(user1.logout())
print(User.active_users)

# Bank Account OOP Exercise
class BankAccount:

    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

acct = BankAccount("Darcel")

print(acct.owner)
print(acct.balance)
print(acct.deposit(20))
print(acct.withdraw(3))
print(acct.balance)
