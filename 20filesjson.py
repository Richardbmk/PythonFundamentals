# Extra Fancy JSON Pickling
import json

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles", "Tabby")

j = json.dumps(["foo", {"bar": ("baz", None, 1.0, 2)}])
j = json.dumps(c.__dict__)

print(j)

## EXEMPLE WITH JSONPCKLE (YOUR HAVE TO INSTALL THE PACKEGE)

import jsonpickle

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

# c = Cat("Charles", "Tabby")

# frozen = jsonpickle.encode(c)
# print(frozen)

with open("catpicke.jason", "w") as file:
	frozen = jsonpickle.encode(c)
	file.write(frozen)


with open("catpicke.jason", "r") as file:
	contents = file.read()
	unfrozen = jsonpickle.decode(contents)
	print(unfrozen)


""" EXERCISE SECCION """
# updates_users
# COLT SOLUTION
import csv

def update_users(old_first, old_last, new_first, new_last):
	with open("users.csv") as csvfile:
		csv_reader = csv.reader(csvfile)
		rows = list(csv_reader)

	count = 0
	with open("user.csv", "w") as csvfile:
		csv_writer = csv.writer(csvfile)
		for row in rows:
			if row[0] == old_first and row[1] == old_last:
				csv_writer.writerow([new_first, new_last])
				count = +1
			else:
				csv_writer.writerow(row)

		return f"Users update: {count}."


# delete_users
# COLT SOLUTION

import csv

def delete_users(first_name, last_name):
	with open("users.csv") as csvfile:
		csv_reader = csv.reader(csvfile)
		rows = list(csv_reader)

	count = 0
	with open("users.csv", "w") as csvfile:
		csv_writer = csv.writer(csvfile)
		for row in rows:
			if row[0] == first_name nad row[1] == last_name:
				count += 1
			else:
				csv_writer.writerow(row)

		return "Users delete: {count}"
