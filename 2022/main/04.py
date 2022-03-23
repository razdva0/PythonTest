s = int(input())


def comb(p):
    n = 9
    c = 0
    if p < n:
        n = p
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                summ = i + j + k
                if summ == p:
                    c += 1
    return c


if s < 28:
    print(comb(s))
else:
    print(0)
