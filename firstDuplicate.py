"""Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal index."""

# O(n) and O(n)
def firstDuplicate(a):
    new_list = []
    for i in a:
        if i in new_list:
            return i
        new_list.append(i)
    return -1
    
# O(n) and O(1)
# Use dictionary instead of List
def firstDuplicate(a):
    d = {}
    for i in a:
        if i in d:
            return i 
        d[i] = 1
    return -1
