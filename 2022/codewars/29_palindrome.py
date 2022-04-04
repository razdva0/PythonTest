def palindrome(num):
    if type(num) != int or num < 0:
        return "Not valid"
    #  return num == int(str(num)[::-1])
    i = 1
    num = str(num)
    while i < len(num) / 2:
        if num[i - 1] != num[-i]:
            return False
        i += 1
    return True


if palindrome(1221) == True:
    print(1221, 'OK')

if palindrome(123322) == False:
    print(123322, 'OK')

if palindrome("ACCDDCCA") == "Not valid":
    print("ACCDDCCA", 'OK')

if palindrome("1221") == "Not valid":
    print("1221", 'OK')
