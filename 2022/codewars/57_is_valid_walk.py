def is_valid_walk(walk):
    dct = {'n': 0, 's': 0, 'e': 0, 'w': 0}
    for x in walk:
        dct[x] += 1
    return len(walk) == 10 and dct['n'] == dct['s'] and dct['e'] == dct['w']
    # return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


if is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']):
    print('OK')
if not is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']):
    print('OK')
if not is_valid_walk(['w']):
    print('OK')
if not is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']):
    print('OK')