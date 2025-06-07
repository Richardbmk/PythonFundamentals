""" 
Task
Read an integer N . For all non-negative integers i < N, print i*i. See the sample for details.

"""

# My solution

n = int(input())

for i in range(n):
    print(i*i)


# Others solution1
[print(i**2) for i in range(n)]


# Others solution2
counter = 0
while counter < n :
    print(counter**2)
    counter += 1