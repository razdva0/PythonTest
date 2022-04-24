def count_change(money, coins):
    results = [0] * (money + 1)
    results[0] = 1
    for i in coins:
        for j in range(i, money + 1):
            results[j] += results[j - i]
    return results[money]


if count_change(4, [1, 2]) == 3:
    print('OK')
else:
    print(count_change(4, [1, 2]))
if count_change(10, [5, 2, 3]) == 4:
    print('OK')
else:
    print(count_change(10, [5, 2, 3]))
if count_change(11, [5, 7]) == 0:
    print('OK')
else:
    print(count_change(11, [5, 7]))
