def odd_or_even(arr):
    return 'odd' if sum(arr) % 2 == 1 else 'even'


if odd_or_even([0, 1, 2]) == "odd":
    print('OK')
if odd_or_even([0, 1, 3]) == "even":
    print('OK')
if odd_or_even([1023, 1, 2]) == "even":
    print('OK')
