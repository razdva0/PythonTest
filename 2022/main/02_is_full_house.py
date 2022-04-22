def is_full_house(lst):
    return all([lst.count(i) >= 2 for i in lst])


if is_full_house(['A', 'K', 'A', 'A', 'K']):
    print('OK')
if not is_full_house(['3', 'J', 'J', '3', '2']):
    print('OK')
if not is_full_house(['A', 'A', 'A', 'A', 'K']):
    print('OK')
