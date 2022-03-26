def stock_list(listOfArt, listOfCat):
    result = ''
    dct = {}
    for x in listOfCat:
        for z in listOfArt:
            z1 = z.split()
            if x == z[0]:
                if x in dct:
                    dct[x] += int(z1[1])
                else:
                    dct[x] = int(z1[1])
            elif not x in dct:
                dct[x] = int(0)
    for x, y in dct.items():
        if len(result) > 0:
            result += ' - '
        result += '(' + x + ' : ' + str(y) + ')'
    return result


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c))
if stock_list(b, c) == '(A : 0) - (B : 1290) - (C : 515) - (D : 600)':
    print('OK')
else:
    print('NO')
