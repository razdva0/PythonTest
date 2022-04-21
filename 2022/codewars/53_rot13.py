def rot13(message):
    result = ''
    for x in message:
        if 'a' <= x <= 'm' or 'A' <= x <= 'M':
            result += chr(ord(x) + 13)
        elif 'n' <= x <= 'z' or 'N' <= x <= 'Z':
            result += chr(ord(x) - 13)
        else:
            result += x
    return result
    # return message.encode('rot13')


if rot13("test") == "grfg":
    print('OK')
else:
    print(rot13('test'))
if rot13("Test") == "Grfg":
    print('OK')
else:
    print(rot13('Test'))
