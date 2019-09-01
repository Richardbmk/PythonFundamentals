print("---------My solution------------------")

# Create a list called instructors
instructors = []
# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.insert(0, "Colt")
instructors.insert(1, "Blue")
instructors.insert(2, "Lisa")
# Run the tests to make sure you've done this correctly!
instructors

print("---------COLT SOLUTION 1------------------")
# Create a list called instructors
instructors = []
# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"

instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")
instructors

print("---------COLT SOLUTION 2------------------")

# Create a list called instructors
instructors = []
# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"
# Use any of the list methods we've seen to accomplish this:
instructors.extend(["Colt", "Blue", "Lisa"])
instructors
