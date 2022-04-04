def palindrome(num, s):
    result = []
    if type(num) != int or type(s) != int or num < 0 or s < 0:
        return 'Not valid'
    while s > len(result):
        if len(str(num)) > 1:
            if num == int(str(num)[::-1]):
                result.append(num)
        num += 1
    return result



if palindrome(6,4) == [11,22,33,44]:
    print('OK')
else:
    print('NO')

if palindrome(75,1) == [77]:
    print('OK')
else:
    print('NO')

if palindrome(19,3) == [22,33,44]:
    print('OK')
else:
    print('NO')

if palindrome(101,2) == [101,111]:
    print('OK')
else:
    print('NO')

if palindrome("ACCDDCCA",3) == "Not valid":
    print('OK')
else:
    print('NO')

if palindrome(773,"1551") == "Not valid":
    print('OK')
else:
    print('NO')

if palindrome(-4505,15) == "Not valid":
    print('OK')
else:
    print('NO')
