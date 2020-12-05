""" 
 list_check(): 

list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True

"""
# Solution 1 (WRONG)

def list_check(lists):
    return type(type(lists)) == list

list_check([[],[1],[2,3]]) 

# Solution 2 (AIN'T WORK)
def list_check(lists):
    return type(lists) is list

list_check([[],[1],[2,3]]) 

# COLT SOLUTON 
def list_check(vals):
    return all(type(l) == list for l in vals)

