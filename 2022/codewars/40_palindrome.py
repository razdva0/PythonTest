def is_palindrome(string):
    #  lst = [*filter(str.isalpha, string.lower())]
    tmp = [x for x in string.upper() if 65 <= ord(x) <= 90]
    return tmp == tmp[::-1]


if is_palindrome('ave coder') == False:
    print('OK')
else:
    print(is_palindrome('ave coder'))

if is_palindrome("Madam, I'm Adam") == True:
    print('OK')
else:
    print(is_palindrome("Madam, I'm Adam"))