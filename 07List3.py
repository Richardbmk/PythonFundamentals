# Create a list called instructors
instructors = []
# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa" ])
# Remove the last value in the list
instructors.pop()
# Remove the first value in the list
instructors.pop(0)
# Add the string "Done" to the beginning of the list
instructors.insert(0, "Done")
# Run the tests to make sure you've done this correctly!

##List slice with negatvies
#some_list[start:end:step]
#some_list[start:end]
first_list = [1, 2, 3, 4, 5, 6]
first_list[1::-1] #[2, 1]
first_list[:1:-1] #[6, 5, 4, 3]
first_list[2::-1] #[3, 2, 1]

#Triki stuff
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ["a", "b", "c"]

#more interesting stuff
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
sounds[::2]
sounds[::-1]
sounds[0]
sounds[5]
sounds[5][::-1]


#SWaping values
names = ["James", "Michele"]
names[0], names[1] = names[1], names[0]
names
