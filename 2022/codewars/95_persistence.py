from math import prod


def persistence(n):
    i = 0
    while len(str(n)) > 1:
        n = prod(list(map(int, str(n))))
        i += 1
    return i


assert persistence(39) == 3
assert persistence(4) == 0
assert persistence(25) == 2
assert persistence(999) == 4
