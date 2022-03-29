import itertools


def choose_best_sum(t, k, ls):
    ls = sorted(ls)
    lst = [sum(ls[:k])]
    if lst[0] > t or len(ls) < k:
        return None
    lst = list(itertools.combinations(ls, k))
    tmp1 = [sum(x) for x in lst if sum(x) <= t]
    return max(tmp1)


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

if choose_best_sum(3760, 17, xs) == 3654:
    print('OK')
else:
    print(choose_best_sum(3760, 17, xs), 'need', 3654)
if choose_best_sum(230, 4, xs) == 230:
    print('OK')
else:
    print(choose_best_sum(230, 4, xs), 'need', 230)
if choose_best_sum(430, 5, xs) == 430:
    print('OK')
else:
    print(choose_best_sum(430, 5, xs), 'need', 430)
if choose_best_sum(430, 8, xs) == None:
    print('OK')
else:
    print(choose_best_sum(430, 8, xs), 'need None')
