""" 
remove_every_other()

remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 

"""
# Solution 1 (WRONG)

def remove_every_other(top):
    if type(top) is list:
        top.pop(1)
        return top
    else:
        return "Is not a list"

remove_every_other([5,1,2,4,1])

# COLT SOLUTION

def remove_every_other(lst):
    return [val for i,val in enumerate(lst) if i % 2 == 0]

