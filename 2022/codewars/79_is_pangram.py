import string
from icecream import ic  # pip install icecream


def is_pangram(s):
    return all([x in s.upper() for x in string.ascii_uppercase])


pangram = "The quick, brown fox jumps over the lazy dog!"
if is_pangram(pangram):
    print('OK')
else:
    ic(is_pangram(pangram))
pangram = "The quick, bron fox jumps over the lazy dog!"
if not is_pangram(pangram):
    print('OK')
else:
    ic(is_pangram(pangram))
