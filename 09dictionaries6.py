#Exercise
print("-------- My Solution -----------")

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(0,len(list1))}
print(answer)

print("-------- COLT SOLUTION 1 -----------")

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0,3)}

print("-------- COLT SOLUTION 2 -----------")

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

dict(zip(list1,list2))  
