"""
Exercise 14
The arithmetic sequence is given with the following formula:

a_n = 10 + 4

Calculate the sum of the first ten elements of this sequence. Print the result to the console as shown below.
"""

# My solution
n_total = 0 

for n in range(1,11):
    n_10 = 10 + 4*n
    n_total += n_10

#print(n_total)
print(f"The sum of the first 10 elements in a sequence: {n_total:.1f}")

# Others solution
