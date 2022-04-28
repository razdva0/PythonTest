def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    finish = n / 2
    i = 0
    result = ' ' * i + '*' * n + '\n'
    n -= 1
    while n > finish:
        i += 1
        result += ' ' * i + '*' * (n - i) + '\n'
        result = ' ' * i + '*' * (n - i) + '\n' + result
        n -= 1
    return result


print(diamond(11))