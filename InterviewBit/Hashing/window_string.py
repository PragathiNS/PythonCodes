def create_freq(s):
    dd = {}
    for i in s:
        if i in dd.keys():
            dd[i] += 1
        else:
            dd[i] = 1
    return (dd)

def minWindow(A, B):
    """
    A = "ADOBECODEBANC"
    B = "ABC"
    ret = "BANC"
    """
    A_dict = create_freq(A)
    B_dict = create_freq(B)
    print (A_dict)
    print (B_dict)
    count = sum(B_dict.values())
    print (count)
    #for i in A:

    

A = "ADOBECODEBANC"
B = "ABC"
minWindow(A, B)
