from math import isqrt


def sum_of_divisors(n):
    result = 1
    div = 1
    while True:
        for div in range(div + 1, isqrt(n) + 1):
            if not n % div:
                mul = 1
                while not n % div:
                    n //= div
                    mul = 1 + mul * div
                result *= mul
                break
        else:
            if n > 1:
                result *= 1 + n
            return result


def buddy(start, limit):
    def s(n):
        return sum_of_divisors(n) - n
    for n in range(start, limit + 1):
        m = s(n) - 1
        if m > n and s(m) == n + 1:
            return [n, m]
    return 'Nothing'


if buddy(10, 50) == [48, 75]:
    print('OK')
if buddy(2177, 4357) == "Nothing":
    print('OK')
if buddy(57345, 90061) == [62744, 75495]:
    print('OK')
if buddy(1071625, 1103735) == [1081184, 1331967]:
    print('OK')
