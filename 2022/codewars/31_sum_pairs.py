def get_unique_numbers(numbers):
    unique = {}
    lst = []
    for number in numbers:
        if number not in unique:
            unique[number] = 1
            lst.append(number)
        elif unique[number] == 1:
            unique[number] = 2
            lst.append(number)
    return list(lst)


def sum_pairs(ints, s):
    result = []
    i = 0
    ints = get_unique_numbers(ints)
    while i < len(ints):
        j = i + 1
        while j < len(ints):
            tmp = {}
            if ints[i] + ints[j] == s:
                tmp[i] = ints[i]
                tmp[j] = ints[j]
            j += 1
            if len(tmp) > 0:
                result.append(tmp)
        i += 1
    if len(result) == 0:
        return
    minimum = max(result[0].keys())
    tmp = [*result[0].values()]
    for x in result:
        if max(x.keys()) < minimum:
            minimum = max(x.keys())
            tmp = [*x.values()]
    return tmp


l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]

if sum_pairs(l1, 8) == [1, 7]:
    print('OK')
else:
    print('NO')
if sum_pairs(l2, -6) == [0, -6]:
    print('OK')
else:
    print('NO')
if sum_pairs(l3, -7) == None:
    print('OK')
else:
    print('NO')
if sum_pairs(l4, 2) == [1, 1]:
    print('OK')
else:
    print('NO')
if sum_pairs(l5, 10) == [3, 7]:
    print('OK')
else:
    print('NO')
if sum_pairs(l6, 8) == [4, 4]:
    print('OK')
else:
    print('NO')
if sum_pairs(l7, 0) == [0, 0]:
    print('OK')
else:
    print('NO')
if sum_pairs(l8, 10) == [13, -3]:
    print('OK')
else:
    print('NO')


'''
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
'''