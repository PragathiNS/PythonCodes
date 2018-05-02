"""A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
"""

def colorful(A):
    sA = str(A)
    len_sA = len(sA)
    if len_sA == 1:
        return (1)
    dig_list = []
    for i in range(len_sA):
        for j in range(i, len_sA):
            dig_list.append(int(sA[i:j + 1]))
    mul = {}
    for val in dig_list:
        m = 1
        for v in str(val):
            m *= int(v)
        if m in mul:
            return (0)
        else:
            mul[m] = 1
    return (1)

print (colorful(0))
print (colorful(111))
print (colorful(3245))
