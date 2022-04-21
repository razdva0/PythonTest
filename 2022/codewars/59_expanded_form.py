def expanded_form(num):
    result = []
    for n, x in enumerate(str(num)):
        if int(x) != 0:
            result.append(int(x) * 10 ** (len(str(num)) - (n + 1)))
    return " + ".join(list(map(str, result)))


if expanded_form(12) == '10 + 2':
    print('OK')
if expanded_form(42) == '40 + 2':
    print('OK')
if expanded_form(70304) == '70000 + 300 + 4':
    print('OK')
