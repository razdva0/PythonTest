def decompose(n):
    num = n.split('/')
    summary = 0
    result = []
    if len(num) == 1:
        num[0] = float(num[0])
        if num[0] == 0:
            return result
        n = float(n)
    if len(num) == 2:
        n = int(num[0]) / int(num[1])
    if n % 1 == 0:
        return [str(int(n))]
    i = 2
    while summary < n:
        if summary + 1 / i <= n:
            result.append(f"1/{i}")
            summary += 1 / i
        i += 1
    return result


if decompose('0') == []:
    print('OK')
else:
    print(decompose('0'))
if decompose('3/4') == ["1/2", "1/4"]:
    print('OK')
else:
    print(decompose('3/4'))
if decompose('4/5') == ["1/2", "1/4", "1/20"]:
    print('OK')
else:
    print(decompose('4/5'))
if decompose('0.74') == ["1/2", "1/5", "1/25"]:
    print('OK')
else:
    print(decompose('0.74'))
if decompose('75/3') == ["25"]:
    print('OK')
else:
    print(decompose('75/3'))
