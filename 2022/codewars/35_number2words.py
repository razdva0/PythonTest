def one_hundred(n, i):
    result = ''
    if i == 0 or i == 2:
        result += {0: 'zero',
                   1: 'one',
                   2: 'two',
                   3: 'three',
                   4: 'four',
                   5: 'five',
                   6: 'six',
                   7: 'seven',
                   8: 'eight',
                   9: 'nine',
                   10: 'ten',
                   11: 'eleven',
                   12: 'twelve',
                   13: 'thirteen',
                   14: 'fourteen',
                   15: 'fifteen',
                   16: 'sixteen',
                   17: 'seventeen',
                   18: 'eighteen',
                   19: 'nineteen'}.get(n)
    if i == 1:
        result += {2: 'twenty',
                   3: 'thirty',
                   4: 'forty',
                   5: 'fifty',
                   6: 'sixty',
                   7: 'seventy',
                   8: 'eighty',
                   9: 'ninety'}.get(n, '')
    if i == 2:
        result += ' hundred'
    return result


def one_thousand(n, i):
    result = ''
    j = 0
    while n > 0:
        if j == 0 and n % 100 < 20 and n % 100 > 0:
            result = one_hundred(n % 100, j) + result
            n = n // 10
            j += 1
        elif n % 10 > 0:
            if j == 1 and len(result) > 0:
                result = one_hundred(n % 10, j) + '-' + result
            elif j == 2 and len(result) > 0:
                result = one_hundred(n % 10, j) + ' ' + result
            else:
                result = one_hundred(n % 10, j) + result
        n = n // 10
        j += 1
    else:
        pass
    if i == 1:
        result += ' thousand'
    return result


def number2words(n):
    """ works for numbers between 0 and 999999 """
    result = ''
    i = 0
    if n < 20:
        result = one_hundred(n, i) + result
    else:
        while n > 0:
            if len(result) > 0:
                result = one_thousand(n % 1000, i) + ' ' + result
            else:
                result = one_thousand(n % 1000, i) + result
            n = n // 1000
            i += 1
    return result


if number2words(0) == "zero":
    print('OK')
else:
    print('NONONONO')
if number2words(1) == "one":
    print('OK')
else:
    print('NONONONO')
if number2words(8) == "eight":
    print('OK')
else:
    print('NONONONO')
if number2words(10) == "ten":
    print('OK')
else:
    print('NONONONO')
if number2words(19) == "nineteen":
    print('OK')
else:
    print('NONONONO')
if number2words(20) == "twenty":
    print('OK')
else:
    print('NONONONO')
if number2words(22) == "twenty-two":
    print('OK')
else:
    print('NONONONO')
if number2words(54) == "fifty-four":
    print('OK')
else:
    print('NONONONO')
if number2words(80) == "eighty":
    print('OK')
else:
    print('NONONONO')
if number2words(98) == "ninety-eight":
    print('OK')
else:
    print('NONONONO')
if number2words(100) == "one hundred":
    print('OK')
else:
    print('NONONONO')
if number2words(301) == "three hundred one":
    print('OK')
else:
    print('NONONONO')
if number2words(793) == "seven hundred ninety-three":
    print('OK')
else:
    print('NONONONO')
if number2words(800) == "eight hundred":
    print('OK')
else:
    print('NONONONO')
if number2words(650) == "six hundred fifty":
    print('OK')
else:
    print('NONONONO')
if number2words(1000) == "one thousand":
    print('OK')
else:
    print('NONONONO')
if number2words(1003) == "one thousand three":
    print('OK')
else:
    print('NONONONO')
