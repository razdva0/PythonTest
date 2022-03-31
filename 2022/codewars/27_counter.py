def counter():
    i = 0

    def func():
        nonlocal i
        i += 1
        return i
    return func


counter_function = counter()
if counter_function() == 1:
    print('OK')
else:
    print('NO')
if counter_function() == 2:
    print('OK')
else:
    print('NO')

counter_one = counter()
counter_two = counter()
if counter_one() == 1:
    print('OK')
else:
    print('NO')
if counter_one() == 2:
    print('OK')
else:
    print('NO')
if counter_two() == 1:
    print('OK')
else:
    print('NO')
if counter_two() == 2:
    print('OK')
else:
    print('NO')