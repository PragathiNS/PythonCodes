def flatten_list(nested_list):
    ret_list = []
    for item in nested_list:
        if type(item) == type([]):
            ret_list.extend(flatten_list(item))
        else:
            ret_list.append(item)
    return ret_list
    
    
print (flatten_list([[],[]]))
print (flatten_list([]))
print (flatten_list([0,[1, 2],[3], [4,[5,6]], 7]))
