print("------- my solution -----------")
for i in range(1, 21, 1):
	if (i%2) == 0 and i != 4:
		print(f"{i} is even number")
	elif i == 4 or i == 13:
		print(f"{i} is unlucky number")
	else:
		print(f"{i} is odd number")

print("------- COLT SOLUTION 1 -----------")

for i in range(1, 21):
	if i == 4 or i == 13:
			print(f"{i} is unlucky number")
	elif (i % 2) == 0:
		print(f"{i} is even number")
	else:
		print(f"{i} is odd number")

print("------- COLT SOLUTION 2 -----------")

for i in range(1, 21):
	if i == 4 or i == 13:
			state = "unlucky"
	elif (i % 2) == 0:
		state = "even"
	else:
		state = "odd"

	print(f"{i} is {state} number")
