def get_count(sentence):
    return len([x for x in sentence if x in 'aeiouAEIOU'])


if get_count("aeiou") == 5:
    print('OK')
if get_count("y") == 0:
    print('OK')
if get_count("bcdfghjklmnpqrstvwxz y") == 0:
    print('OK')
if get_count("") == 0:
    print('OK')
if get_count("abracadabra") == 5:
    print('OK')