def sum_of_cubs(string):
    return sum([int(x) ** 3 for x in string]) % 2 == 0


def add_tmp(tmp):
    if sum_of_cubs(tmp):
        tmp = tmp[::-1]
    else:
        tmp = tmp[1:] + tmp[0]
    return tmp


def revrot(strng, sz):
    if sz <= 0 or not strng or sz > len(strng):
        return ''
    result = []
    tmp = ''
    for x in strng:
        if len(tmp) == sz:
            result.append(add_tmp(tmp))
            tmp = ''
        tmp += x
    if len(tmp) == sz:
        result.append(add_tmp(tmp))
    return ''.join(result)


if revrot("1234", 0) == "":
    print('OK')
else:
    print(revrot("1234", 0))
if revrot("", 0) == "":
    print('OK')
else:
    print(revrot("", 0))
if revrot("1234", 5) == "":
    print('OK')
else:
    print(revrot("1234", 5))
s = "733049910872815764"
if revrot(s, 5) == "330479108928157":
    print('OK')
else:
    print(revrot(s, 5))
