
# Methods explanation

file = open("story.txt")
file.seek(0) # Put the cursor at the beggining
print(file)
# print(file.read()) # Read all the document
# print(file.readline()) # Read line by line
print(file.readlines()) # Read all lines and put every line in a list
file.close() # We used to close the file


# Methods open and close files

# Another way to doy the same thing.
file = open("story.txt")
print(file.read())
print(file.close())
print(file.closed) # Give True o Fase, depending is the file is open or not


# # Methods open and close files automatically

with open("story.txt") as file:
	print(file.read())
print(file.closed)


# Write things inside a file

with open("lonely.txt", "w") as file:
	file.write("The lonely, is a kind of sicknes\n")
	file.write("that make you feel alone, even if you have\n")
	file.write("people by you side, that love you.\n")

# There's no need to create the file to write things inside.

with open("laugh.txt", "w") as file:
	file.write("HAHAHAHAHAHAHAH" * 10000)


# a -  Append to a file (previous contents not removed)

with open("lonely.txt", "a") as file:
	file.write("There is a group of men\n")
	file.write("that that find a cure for this sickness\n")
	file.write("...")


# r+ - Read and write to a file (writing based on cursor)

# with open("laugh.txt", "r+") as doc:
# 	doc.write("I can hear you... HAHAHAH")

with open("laugh.txt", "r+") as doc:
	doc.write(" ? ")
	doc.seek(10)
	doc.write(" ? ")


# FILES EXERCISES...

def copy(file):
	with open("file1.txt") as doc:
		info = doc.write("Copy this info in another file please...")
