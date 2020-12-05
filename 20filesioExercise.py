FILES EXERCISES...

# Copy exercies
def copy(file_name, new_file_name):
	with open(file_name) as file:
		file.seek(0)
		text = file.read()

		with open(new_file_name, "w") as new_doc:
			new_doc.write(text)


copy('lonely.txt', 'story_copy.txt')

# Exercise Copy_and_reverse
# My solution
def Copy_and_reverse(file_name, new_file_name):
	with open(file_name) as file:
		file.seek(0)
		text = file.read()

		with open(new_file_name, "w") as new_doc:
			new_doc.writelines(reversed(text))

Copy_and_reverse('lonely.txt', 'story_copy.txt')

# Colt solution. THE OUT PUT IS THE SAME!!!
def Copy_and_reverse(file_name, new_file_name):
	with open(file_name) as file:
		text = file.read()

		with open(new_file_name, "w") as new_doc:
			new_doc.write(text[::-1])



Copy_and_reverse('lonely.txt', 'story_copy1.txt')
My solution
def statistics1(file_name):
	with open(file_name) as file:
		text = file.read()
		numOfchars = len(text)
		numOfWords = len(text.split())
		numOfLines = len(text.splitlines())
	return { "lines" : numOfLines,
				 "words" : numOfWords,
				 "characters" : numOfchars
		}

statistics('lonely.txt')

COlt Solution. THE OUTPUT IS THE same
def statistics2(file_name):
	with open(file_name) as file:
		lines = file.readlines()

	return { "lines" : len(lines),
			 "words" : sum(len(line.split(" ")) for line in lines),
			 "characters" : sum(len(line) for line in lines) }

statistics1('lonely.txt')
print(statistics2('lonely.txt'))

def find_and_replace(file_name, old_word, new_word):
	with open(file_name, "r+") as file:
		text = file.read()
		new_text = text.replace(old_word, new_word)
		file.seek(0)
		file.write(new_text)
		file.truncate()

find_and_replace("lonely.txt", "sickness", "desease")
