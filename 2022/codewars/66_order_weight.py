def order_weight(strng):
    dct = {}
    result = []
    for x in strng.split():
        if sum([int(z) for z in x]) in dct:
            dct[sum([int(z) for z in x])].append(x)
        else:
            dct[sum([int(z) for z in x])] = [x]
    for x in sorted(dct.items(), key=lambda s: s[0]):
        for z in sorted(x[1], key=lambda s: s):
            result.append(z)
    return ' '.join(x for x in result)
    # return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))


if order_weight("103 123 4444 99 2000") == "2000 103 123 4444 99":
    print('OK')
else:
    print(order_weight("103 123 4444 99 2000"))
if order_weight("2000 10003 1234000 44444444 9999 11 11 22 123") == "11 11 2000 10003 22 123 1234000 44444444 9999":
    print('OK')
else:
    print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
if order_weight("") == "":
    print('OK')
else:
    print(order_weight(""))
