def likes(names):
    end = 'likes this'
    end_23 = 'like this'
    if len(names) == 0:
        return f'no one {end}'
    if len(names) == 1:
        return f'{names[0]} {end}'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} {end_23}'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} {end_23}'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others {end_23}'


if likes([]) == 'no one likes this':
    print('OK')
if likes(['Peter']) == 'Peter likes this':
    print('OK')
if likes(['Jacob', 'Alex']) == 'Jacob and Alex like this':
    print('OK')
if likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this':
    print('OK')
if likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this':
    print('OK')
