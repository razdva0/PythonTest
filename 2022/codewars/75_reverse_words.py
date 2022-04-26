from icecream import ic  # pip install icecream


def reverse_words(text):
    return ' '.join(s[::-1] for s in text.split(' '))


if reverse_words('The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god':
    print('OK')
else:
    ic(reverse_words('The quick brown fox jumps over the lazy dog.'))
if reverse_words('apple') == 'elppa':
    print('OK')
else:
    ic(reverse_words('apple'))
if reverse_words('a b c d') == 'a b c d':
    print('OK')
else:
    ic(reverse_words('a b c d'))
if reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow':
    print('OK')
else:
    ic(reverse_words('double  spaced  words'))

