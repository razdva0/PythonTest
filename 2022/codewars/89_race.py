def race(v1, v2, g):
    if v1 >= v2: return None
    k = 0
    first = v1 / 360000
    second = v2 / 360000
    i = 0
    while k < g:
        g += first
        k += second
        i += 1
    result = [i // 360000, i // 6000 % 60, i % 6000 // 100]
    return result


if race(720, 850, 70) == [0, 32, 18]: print('OK')
else: print(race(720, 850, 70))
if race(80, 91, 37) == [3, 21, 49]: print('OK')
else: print(race(80, 91, 37))
if not race(820, 81, 550): print('OK')
else: print(race(820, 81, 550))
