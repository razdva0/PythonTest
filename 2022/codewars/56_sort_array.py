def sort_array(source_array):
    odd = sorted([x for x in source_array if x % 2 == 1])
    return [x if x % 2 == 0 else odd.pop(0) for x in source_array]



if sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]:
    print('OK')
else:
    print(sort_array([5, 3, 2, 8, 1, 4]))
if sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]:
    print('OK')
else:
    print(sort_array([5, 3, 1, 8, 0]))
if sort_array([]) == []:
    print('OK')
else:
    print(sort_array([]))