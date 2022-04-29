def increment_string(strng):
    numbers = []
    for x in strng[::-1]:
        if x.isdigit():
            numbers.insert(0, x)
        else:
            break
    if not numbers:
        string = strng
        num = '1'
    else:
        string = ''.join(x for x in strng[:-len(numbers)])
        num = str.zfill(str(int(''.join(numbers)) + 1), len(numbers))
    return string + num


if increment_string("foo") == "foo1":
    print('OK')
else:
    print(increment_string("foo"))
if increment_string("foobar001") == "foobar002":
    print('OK')
if increment_string("foobar1") == "foobar2":
    print('OK')
if increment_string("f1oobar01") == "f1oobar02":
    print('OK')
if increment_string("foobar99") == "foobar100":
    print('OK')
if increment_string("foobar099") == "foobar100":
    print('OK')
if increment_string("") == "1":
    print('OK')
