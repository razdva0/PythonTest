def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


if validate_pin("1") == False:
    print('OK')
if validate_pin("12") == False:
    print('OK')
if validate_pin("123") == False:
    print('OK')
if validate_pin("12345") == False:
    print('OK')
if validate_pin("1234567") == False:
    print('OK')
if validate_pin("-1234") == False:
    print('OK')
if validate_pin("-12345") == False:
    print('OK')
else:
    print(validate_pin("-12345"))
if validate_pin("1.234") == False:
    print('OK')
if validate_pin("00000000") == False:
    print('OK')
