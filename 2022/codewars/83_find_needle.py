def find_needle(haystack):
    return f'found the needle at position {[num for num, x in enumerate(haystack) if x == "needle"][0]}'
    # return f'found the needle at position {haystack.index("needle")}'


if find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]) == 'found the needle at position 3':
    print('OK')
else:
    print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
if find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']) == 'found the needle at position 5':
    print('OK')
else:
    print(find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']))
if find_needle([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54]) == 'found the needle at position 30':
    print('OK')
else:
    print(find_needle([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54]))
