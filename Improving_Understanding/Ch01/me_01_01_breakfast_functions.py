""" A Functional Breakfast """
cheese = "cheddar"

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')



def make_omelette():
    global cheese
    cheese = "Swiss"
    mix_and_cook()
    omelette = 'a {} omelette'.format(cheese)
    return omelette

def make_pancakes():
    mix_and_cook()
    omelette = 'a tasty omelette with {}'.format(cheese)
    return omelette

def fancy_omlette(*ingredients):
    mix_and_cook()
    omelette = 'a fancy omelette with {} ingredients'.format(len(ingredients))
    #omelette = 'a fancy omelette with {} ingredients'.format(ingredients)
    return omelette

#make = fancy_omlette('Juice','bacon','bread','Orange')

#print(fancy_omlette('Juice','bacon','bread','Orange'))

print(make_omelette())
print("###################")
print(make_pancakes())
print("###################")
print(cheese)