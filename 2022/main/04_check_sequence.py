def check_sequence(lst):
    check = [1, -1]
    for i in range(len(lst) - 1):
        if lst[i] - lst[i + 1] not in check:
            return 0
        else:
            check = [lst[i] - lst[i + 1]]
    return lst[1] - lst[0]


if check_sequence([1, 2, 3]) == 1:
    print('check_sequence OK')
if check_sequence([3, 2, 1]) == -1:
    print('check_sequence OK')
if check_sequence([1, 2, 1]) == 0:
    print('check_sequence OK')
if check_sequence([1, 1, 2]) == 0:
    print('check_sequence OK')


def check_sequence2(lst):
    if sorted(set(lst)) == lst:
        return 1
    if sorted(set(lst), reverse=True) == lst:
        return -1
    return 0


if check_sequence2([1, 2, 3]) == 1:
    print('check_sequence2 OK')
if check_sequence2([3, 2, 1]) == -1:
    print('check_sequence2 OK')
if check_sequence2([1, 2, 1]) == 0:
    print('check_sequence2 OK')
if check_sequence2([1, 1, 2]) == 0:
    print('check_sequence2 OK')
