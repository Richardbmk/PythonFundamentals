# Sets cannot have duplictes
s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}

# Creating a new set
s = set({1, 4, 5})

# Creates a set with the same values as above
s = {1, 4, 5}
4 in s
# True
8 in s
# False


for thing in s:
    print(thing)

cities = ["Los angeles", "Boulder", "Kyoto", "Florence", "Tokio", "Barcelona", "Florence", "Los angeles"]
print(set(cities))
print(list(set(cities)))
print(len(set(cities)))

# Set methods

# Methods add
s = set([1, 2, 3])
s.add(4)
s # {1, 2, 3, 4}
s.add(4)
s # {1, 2, 3, 4}

#Method remove
set1 = {1,2,3,4,5,6}
set1.remove(3)
print(set1) # {1, 2, 4, 5, 6}

#Method copy
s = set([1,2,3])
another_s = s.copy()
another_s # {1, 2, 3}
another_s is s # False

#Method clear
s = set([1, 2, 3])
s.clear()
s # set()

# Method set Math
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}
    #Union
math_students | biology_students
    #Intersection
math_students & biology_students
