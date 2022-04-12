def high_and_low(numbers):
    mass = list(map(int, numbers.split()))
    return str(max(mass)) + ' ' + str(min(mass))


if high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9":
    print('OK')
else:
    print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
if high_and_low("1 2 3") == "3 1":
    print('OK')
else:
    print(high_and_low("1 2 3"))
