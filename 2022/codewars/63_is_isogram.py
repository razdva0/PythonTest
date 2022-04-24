def is_isogram(string):
    return all(string.upper().count(x) == 1 for x in string.upper())


if is_isogram("Dermatoglyphics"):
    print('OK')
if is_isogram("isogram"):
    print('OK')
if not is_isogram("aba"):
    print('OK')
if not is_isogram("moOse"):
    print('OK')
if not is_isogram("isIsogram"):
    print('OK')
if is_isogram(""):
    print('OK')
