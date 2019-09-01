x = (1,2,3)
3 in x # True
x[0] = "change me!" # TypeError: 'tuple' object does not support item assignment

first_tuple = (1, 2, 3, 3, 3)

first_tuple[1] // 2
first_tuple[2] // 3
first_tuple[-1] // 3

second_tuple = tuple(5, 1, 2) # ITt doesn't work

second_tuple[0] # 5
second_tuple[-1] # 2

# TUples can be used as keys in dicctionaries
locations = {
    (35.6984, 38.0348): "Tokyo Ofice",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office"
}

locations[(35.6984, 38.0348)] #"Tokyo Ofice"

# Some dicctionary methods like .items() return TUples
cat = {"name": "biscuit", "age": 0.5, "favorite_toy": "my chapstick"}
cat.items() # This method turn it to a Tuple...

# Looping with tuples
names = ('Colt', 'Blue', 'Rusty', 'Lassie')
for name in names:
    print(name)

i = len(names)-1
while i >= 0:
    print(months[i])
    i -= 1

#Method count
x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3

#Method index
t = (1,2,3,3,3)
t.index(1) # 0
t.index(5) # ValueError: tuple.index(x): x not in tuple
t.index(3) # 2 - only the first matching index is returned

# Nested TUples
nums = (1, 2, 3, 4, (5, 6), 7, 8)
nums
nums[0]
nums[4][0]
nums[0:]
nums[0:4]
nums[0:8:2]
