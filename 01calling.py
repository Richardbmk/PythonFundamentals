# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

print(f"actually_sick = {actually_sick}, kinda_sick = {kinda_sick}, hate_your_job = {hate_your_job}, sick_days = {sick_days}")
# NO TOUCHING ======================================


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if actually_sick and sick_days > 0:
    calling_in_sick = True
    print(calling_in_sick)
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
    print(calling_in_sick)
else:
    calling_in_sick = False
    print(calling_in_sick)

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
