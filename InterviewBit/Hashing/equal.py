# Given an array A of integers, find the index of values that satisfy
# A + B = C + D, where A,B,C & D are integers values in the array

def equal(a):
    su = []
    mapp = dict()
    l = len(a)
    for i in range(0, l):
        for j in range(i, l):
            if (i != j):
                summ = a[i] + a[j]
                if summ not in mapp.keys():
                    mapp[summ] = []
                    mapp[summ].append((i,j))
                else:
                    aa = mapp[summ][-1][0]
                    bb = mapp[summ][-1][1]
                    cc = i
                    dd = j
                    if (aa < cc and bb != dd and bb != cc):
                        su.append([aa, bb, cc, dd])
                        mapp[summ].append((i,j))
    return (sorted(su)[0])

#test = [3, 4, 7, 1, 2, 9, 8]
test = [0, 0, 0, 3, 3]
print (equal(test))
