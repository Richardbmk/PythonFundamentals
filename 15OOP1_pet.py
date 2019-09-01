class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

print("Chicken Coop Exercise")
# Chicken Coop Exercise
class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")
print(Chicken.total_eggs)
print(c1.lay_egg())
print(Chicken.total_eggs)
print(c2.lay_egg())
print(c2.lay_egg())

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


# user1 = User("Jua", "Lavanda", 68)
# user2 = User("Mario", "Paquito", 89)
#
# print(user1.display_active_user())
# print(User.display_active_user())
#
# print(User.display_active_user())
# user1 = User("Jua" "Lavanda", 68)
# user2 = User("Mario" "Paquito", 89)
# print(User.display_active_user())

tom = User.from_string("Tom,Jones,75")
print(tom.first)
print(tom.full_name())
print(tom.birthday())
print(tom)

j = User("judy", "Makuere", 25)
j = str(j)
print(j)
