def sum_dig_pow(a, b):
    result = []
    for x in range(a, b + 1):
        s = str(x)
        n = 0
        i = 1
        for z in s:
            n += int(z) ** i
            i += 1
        if x == n:
            result.append(x)
    return result


print(sum_dig_pow(1, 100))
