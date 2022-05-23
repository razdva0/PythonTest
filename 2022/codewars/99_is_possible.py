from itertools import combinations
from time import time


def comb(tpl, database) -> bool:
    for x in tpl:
        for z in database[x]:
            if z in tpl:
                return False
    return True


def is_possible(database: dict) -> bool:
    db = []
    for i in range(1, len(database) + 1):
        db += [x for x in combinations(database, i) if comb(x, database)]
    for x in db:
        for y in db:
            if set(x + y) == database.keys():
                return True
    return False


start = time()
if is_possible({0: [3], 1: [2], 2: [1, 3], 3: [2, 0, 4], 4: [3]}):
    print('1_OK')
if is_possible({0: [2], 1: [7], 2: [0], 3: [4], 4: [9, 3], 5: [8, 9], 6: [], 7: [1], 8: [5], 9: [4, 5]}):
    print('2_OK')
if not is_possible({0: [8, 4], 1: [], 2: [5], 3: [6], 4: [0, 8, 7], 5: [2, 8], 6: [3, 7], 7: [4, 6], 8: [0, 4, 5]}):
    print('3_OK')
print(is_possible({0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0, 5], 4: [1], 5: [3], 6: [7, 8], 7: [6], 8: [6, 9, 10, 11], 9: [8, 11], 10: [8, 11], 11: [9, 10]} ))
end = time()
print(end - start)