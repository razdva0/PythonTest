from time import time


def gap(g, m, n):
    a = list(range(n + 1))
    a[1] = 0
    tmp = -1
    i = 2
    while i <= n:
        if a[i] != 0:
            if a[i] >= m:
                if a[i] - tmp == g:
                    return [tmp, a[i]]
                tmp = a[i]
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1


start = time()
assert gap(2, 100, 110) == [101, 103]
assert gap(4, 100, 110) == [103, 107]
assert not gap(6, 100, 110)
assert gap(8, 300, 400) == [359, 367]
assert gap(10, 300, 400) == [337, 347]
assert gap(2, 100, 103) == [101, 103]
print(gap(15, 1, 10000000))
end = time()
print(end - start)
