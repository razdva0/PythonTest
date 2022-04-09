def ft_length(n):
    length = 0
    for l in range(1, n + 1):
        length += l + 1
    return length


def plant_forest(*args):
    lst = [*args]
    length = ft_length(max(lst))
    result = [''] * length
    for x in lst:
        i = -1
        ladder = length - 1
        tmp_len = ft_length(x)
        j = x
        for z in range(length - 1, -1, -1):
            if length - tmp_len <= z:
                flag = 0
                for k in range(x - 1 - i, -1, -1):
                    tmp = ''
                    tmp += ' ' * (x - k)
                    tmp += '*' * (1 + k * 2)
                    tmp += ' ' * (x - k)
                    if flag != 0 or k != 0:
                        result[ladder] += tmp
                        ladder -= 1
                    flag += 1
            else:
                result[ladder] += ' ' * (1 + x * 2)
                ladder -= 1
            i += 1
            j -= 1
    print('#' * (len(result[0]) + 2))
    for x in result:
        print('#' + x + '#')
    print('#' * (len(result[0]) + 2))


plant_forest(3, 2, 5, 4, 2, 3)  # Рисует ёлочки разной высоты
