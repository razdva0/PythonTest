def nico(key, message):
    result = ''
    lst = []
    tmp = ''
    for x in message:
        if len(tmp) < len(key):
            tmp += x
        else:
            lst.append(tmp)
            tmp = ''
            tmp += x
    while len(tmp) < len(key):
        tmp += ' '
    lst.append(tmp)
    asc = [ord(y) for _, y in enumerate(key)]
    for x in lst:
        dct = {}
        for i, z in enumerate(x):
            dct[asc[i]] = z
        for n in sorted(dct.keys()):
            result += dct[n]
    return result


key, message = "crazy", "secretinformation"
if nico(key, message) == "cseerntiofarmit on  ":
    print('OK')
else:
    print(nico(key, message) + '$')
key, message = "abc", "abcd"
if nico(key, message) == "abcd  ":
    print('OK')
else:
    print(nico(key, message) + '$')
key, message = "ba", "1234567890"
if nico(key, message) == "2143658709":
    print('OK')
else:
    print(nico(key, message) + '$')
key, message = "a", "message"
if nico(key, message) == "message":
    print('OK')
else:
    print(nico(key, message) + '$')
key, message = "key", "key"
if nico(key, message) == "eky":
    print('OK')
else:
    print(nico(key, message) + '$')
key, message = "abcdefgh", "abcd"
if nico(key, message) == "abcd    ":
    print('OK')
else:
    print(nico(key, message) + '$')
