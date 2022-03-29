def find_nb(m):
    n = 1
    result = 0
    while result < m:
        result += n ** 3
        if result == m:
            return n
        n += 1
    return -1


if find_nb(4183059834009) == 2022:
    print('OK')
else:
    print(find_nb(4183059834009))
if find_nb(24723578342962) == -1:
    print('OK')
else:
    print(find_nb(24723578342962))
if find_nb(135440716410000) == 4824:
    print('OK')
else:
    print(find_nb(135440716410000))
if find_nb(40539911473216) == 3568:
    print('OK')
else:
    print(find_nb(40539911473216))
if find_nb(26825883955641) == 3218:
    print('OK')
else:
    print(find_nb(26825883955641))
