def remove_smallest(numbers):
    lst = numbers[:]
    if lst:
        lst.remove(min(lst))
    return lst


if remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5]: print('OK')
if remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4]: print('OK')
if remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1]: print('OK')
if remove_smallest([]) == []: print('OK')
