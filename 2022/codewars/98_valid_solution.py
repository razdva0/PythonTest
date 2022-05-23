def valid_solution(board):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    for x in board:
        if sorted(x) != check:
            return False
        tmp = []
        tmp1 = []
        tmp2 = []
        tmp3 = []
        for num, y in enumerate(board, start=1):
            tmp.append(y[i])
            tmp1 += y[:3]
            tmp2 += y[3:6]
            tmp3 += y[6:]
            if num % 3 == 0:
                if sorted(tmp1) != sorted(tmp2) != sorted(tmp3) != check:
                    return False
                tmp1 = []
                tmp2 = []
                tmp3 = []
        if sorted(tmp) != check:
            return False
        i += 1
    return True


if valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]):
    print('1_OK')

if not valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                       [4, 9, 8, 2, 6, 1, 3, 7, 5],
                       [7, 5, 6, 3, 8, 4, 2, 1, 9],
                       [6, 4, 3, 1, 5, 8, 7, 9, 2],
                       [5, 2, 1, 7, 9, 3, 8, 4, 6],
                       [9, 8, 7, 4, 2, 6, 5, 3, 1],
                       [2, 1, 4, 9, 3, 5, 6, 8, 7],
                       [3, 6, 5, 8, 1, 7, 9, 2, 4],
                       [8, 7, 9, 6, 4, 2, 1, 3, 5]]):
    print('2_OK')
