from collections import deque

def appendn(q, r, c, x, y):
    if (x >= 0 and x < c and y >= 0 and y < r):
        q.append([x,y])

def findParts(M, i, j, r, c):
    q = deque()
    q.append([i,j])
    while (len(q) != 0):
        i = q.pop()
        print ("element popped from queue: ", i)
        y = i[0]
        x = i[1]
        if (M[x][y] == 1):
            M[x][y] = 2
            print (M)
            print ()
            appendn(q, r, c, x + 1, y)
            appendn(q, r, c, x, y + 1)
            appendn(q, r, c, x - 1, y)
            appendn(q, r, c, x, y - 1)

def inslands(M):
    if (M == None or M == [[]]):
        return 0
    islands = 0
    r = len(M)
    c = len(M[0])
    print ("row and col", r, c)
    for i in range(0, r):
        for j in range(0, c):
            if (M[i][j] == 1):
                islands += 1
            findParts(M, i, j, r, c)
    return islands


M = [[1,0,1],[1,1,0],[0,0,0],[0,1,1]]
print (M)
print (inslands([[1,0,1],[1,1,0],[0,0,0],[0,1,1]]))

