def no_volunteer(src, dest):
    steps = 0
    if (src == dest):
        return (steps)

    board = [[0, 1, 2, 3, 4, 5, 6, 7]]
    for i in range(1, 8):
        inner = []
        for j in range(8):
            ele = board[i - 1][j] + 8
            inner.append(ele)
        board.append(inner)

    for i in range(len(board)):
        print (board[i], end='\n')


    src_ind = [(row, val.index(src)) for row, val in enumerate(board) if src in
            val]
    dest_ind = [(row, val.index(dest)) for row, val in enumerate(board) if dest
            in
            val]
    print (src_ind, dest_ind)

    return (1)
    




print (no_volunteer(19, 36))
