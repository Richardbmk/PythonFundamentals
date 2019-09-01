# 266. Iterators vs. Iterables?!?!?

name = "Richard"
# next(name) #TypeError: 'str' object is not an iterator
it = iter(name)
# print(it) # <str_iterator object at 0x006106D0>
# print(next(it)) # R
# print(next(it)) # i
# print(next(it)) # c
# print(next(it)) # h
# print(next(it)) # a
# print(next(it)) # r
# print(next(it)) # d

# for num in [1,2,3]
# for char in "Hi miami"

def my_for(iterable):
    iterable = iter(iterable)
    while True:
        try:
            print(next(iterable))
        except StopIteration:
            break

# my_for("Hi Richard")
# my_for([1,2,3,4])

#######################################
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x*x)

# my_for("lol", print)
# my_for([1,2,3,4,5], square)

#############################################
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

# for x in Counter(0, 10):
#     print(x)
