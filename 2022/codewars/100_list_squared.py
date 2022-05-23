from time import time
from math import sqrt, pow


def multy(n):
    result = []
    x = 1
    m_div = n
    while x <= m_div:
        if n % x == 0:
            m_div = n // x
            result.append(m_div)
            result.append(x)
        x += 1
    return sum(x ** 2 for x in set(result))


def list_squared(m, n):
    result = []
    for x in range(m, n + 1):
        tmp = multy(x)
        if sqrt(tmp) % 1 == 0:
            result.append([x, tmp])
    return result


start = time()
# if list_squared(1, 250) == [[1, 1], [42, 2500], [246, 84100]]:
#     print('1_OK')
# if list_squared(42, 250) == [[42, 2500], [246, 84100]]:
#     print('2_OK')
# if list_squared(250, 500) == [[287, 84100]]:
#     print('3_OK')
print(list_squared(1, 10000))
end = time()
print(end - start)

'''
from math import floor, sqrt, pow

def sum_squared_factors(n):
    s, res, i = 0, [], 1
    while (i <= floor(sqrt(n))):
        if (n % i == 0):
            s += i * i
            nf = n // i
            if (nf != i):
                s += nf * nf
        i += 1
    if (pow(int(sqrt(s)), 2) == s):
        res.append(n)
        res.append(s)
        return res
    else:
        return None
        
def list_squared(m, n):
    res, i = [], m
    while (i <= n):
        r = sum_squared_factors(i)
        if (r != None):
            res.append(r);
        i += 1
    return res
'''
