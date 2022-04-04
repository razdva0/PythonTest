def amount_of_pages(summary):
    result = ''
    i = 0
    while len(result) < summary:
        i += 1
        result += str(i)
    return i


if amount_of_pages(5) == 5:
    print('OK')
if amount_of_pages(25) == 17:
    print('OK')
if amount_of_pages(1095) == 401:
    print('OK')
if amount_of_pages(185) == 97:
    print('OK')
if amount_of_pages(660) == 256:
    print('OK')
