def roman_numerals(num: str):
    dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = [0]
    for x in reversed(num):
        if dct[x] >= result[-1]:
            result.append(dct[x])
        else:
            result[-1] -= dct[x]
    return sum(result)


numerals = 'I'
if roman_numerals(numerals) == 1:
    print('OK')
else:
    print(roman_numerals(numerals))
numerals = 'III'
if roman_numerals(numerals) == 3:
    print('OK')
else:
    print(roman_numerals(numerals))
numerals = 'IV'
if roman_numerals(numerals) == 4:
    print('OK')
else:
    print(roman_numerals(numerals))
numerals = 'V'
if roman_numerals(numerals) == 5:
    print('OK')
else:
    print(roman_numerals(numerals))
numerals = 'X'
if roman_numerals(numerals) == 10:
    print('OK')
else:
    print(roman_numerals(numerals))
numerals = 'L'
if roman_numerals(numerals) == 50:
    print('OK')
else:
    print(roman_numerals(numerals))
numerals = 'C'
if roman_numerals(numerals) == 100:
    print('OK')
else:
    print(roman_numerals(numerals))
numerals = 'D'
if roman_numerals(numerals) == 500:
    print('OK')
else:
    print(roman_numerals(numerals))
numerals = 'M'
if roman_numerals(numerals) == 1000:
    print('OK')
else:
    print(roman_numerals(numerals))
numerals = 'XV'
if roman_numerals(numerals) == 15:
    print('OK')
else:
    print(roman_numerals(numerals))
numerals = 'XCIX'
if roman_numerals(numerals) == 99:
    print('OK')
else:
    print(roman_numerals(numerals))
