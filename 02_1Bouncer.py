# #ask for age
# age = input("How old are you?")
#
# if age != "":
#     if int(age) >= 18 and int(age) < 21:
#         #18-21 wristband
#         print("You can enter, but need a wristband!")
#     if int(age) >= 21:
#         #21+ drink, normal entry
#         print("You are goo to enter and drink!")
#     else:
#         #too young, soory
#         print("You can't come in, little one! :(")
# else:
#     print("Please enter an age!")

#Imporoves verion
# age = input("How old are you?")
#
# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         #18-21 wristband
#         print("You can enter, but nees a wristband!")
#     if age >= 21:
#         #21+ drink, normal entry
#         print("You are goo to enter and drink!")
#     else:
#         #too young, soory
#         print("You can't come in, little one! :(")
# else:
#     print("Please enter an age!")

#Another imporved version
age = input("How old are you: ")
if age:
	age = int(age)
	if age >= 18 and age < 21:
		print("You can enter, but need a wristband!")
	elif age >= 21:
	    print("You are good to enter and can drink!")
	else:
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")