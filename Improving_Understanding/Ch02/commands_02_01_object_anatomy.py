""" What Makes Up an Object? """
# examine a string object
print('# examine a string object')
print('shirt')
print(type('shirt'))
print(dir('shirt'))


# use upper method on a string object
print('# use upper method on a string object')
print('shirt'.upper())

# examine IDs of different string objects
print('# examine IDs of different string objects')
print(id('shirt'))
print(id('pants'))

# examine an integer object
print('# examine an integer object')
print(id(1))
print(dir(1))

# examine ID and attributes of functions
print('# examine ID and attributes of functions')
print(id(id))
print(dir(dir))

"""
class jeans:
    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True

    def take_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False

my_jeans = jeans(32, 33, 'blue')
print(type(my_jeans))
print(dir(jeans))
my_jeans.put_on()
print(my_jeans.wearing)
my_jeans.take_off()
print(my_jeans.wearing)

"""

print('###############################')

class shirt:
    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True

red = shirt()
crimson = shirt()

print(id(red))
print(id(crimson))

print(red.clean)
print(red is crimson)


""" You Can Change an Outfit, But You Can't Change Your Words """

# create a closet full of clothes
closet = ['shirt','hat','pants','jacket','socks']
print(closet)
print(id(closet))

# remove a hat
closet.remove('hat')
print(closet)
print(id(closet))

# create a poor choice of words
words = "You're wearing that"
print(words)
print(id(words))

# add more to the phrase
words = words + ' because you look great!'
print(words)
print(id(words))
