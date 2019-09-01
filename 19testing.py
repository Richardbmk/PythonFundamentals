# # 293. Section Introduction
# # 295. Assertions
#
# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y
#
# # print(add_positive_numbers(1, 1)) # 2
# # print(add_positive_numbers(1, -1)) # AssertionError: Both numbers must be positive!
#
#
# def eat_junk(food):
#     assert food in [
#         "pizza",
#         "ice cream",
#         "candy",
#         "friend butter"
#     ], "food must be a junk food!"
#     return f"NOM NOM NOM I am eating {food}"
#
# # food = input("ENTER A FOOD PLEASE: ")
# # print(eat_junk(food))
#
# # def add(a, b):
# #     """
# #     >>> add(2, 3)
# #     5
# #     >>> add(100, 200)
# #     300
# #     """
# #     return a + b
#
# """to run the code tipe
# python -m doctest -v 19testing.py"""
#
# def double(values):
#     """double the values in a list
#
#     >>> duble([1, 2, 3, 4])
#     [2, 4, 6, 8]
#
#     >>> double([])
#     []
#
#     >>> double(['a', 'b', 'c'])
#     ['aa', 'bb', 'cc']
#
#     >>> double([True, None])
#     Traceback (most recent call last):
#         ...
#     TypeError: unsupported operand types(s) for *: 'int' and 'NoneType'
#     """
#     return [2 * element for element in values]

# def say_hi():
#     """
#     >>> say_hi()
#     'hi'
#     """
#     return "hi"

# def say_true():
#     """
#     >>> say_true()
#     True
#     """
#     return True
#
# def make_dict(keys):
#     """
#     >>> make_dict(['a', 'b'])
#     {'b': True, 'a': True}
#     """
#     return {key: True for key in keys}
