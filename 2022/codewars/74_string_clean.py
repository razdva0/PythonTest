from icecream import ic  # pip install icecream


def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())


value = ''
if string_clean(value) == "":
    print('OK')
else:
    ic(string_clean(value))
value = '! !'
if string_clean(value) == "! !":
    print('OK')
else:
    ic(string_clean(value))
value = '123456789'
if string_clean(value) == "":
    print('OK')
else:
    ic(string_clean(value))
value = '(E3at m2e2!!)'
if string_clean(value) == "(Eat me!!)":
    print('OK')
else:
    ic(string_clean(value))
value = 'Dsa32 cdsc34232 csa!!! 1I 4Am cool!'
if string_clean(value) == "Dsa cdsc csa!!! I Am cool!":
    print('OK')
else:
    ic(string_clean(value))
value = 'A1 A1! AAA   3J4K5L@!!!'
if string_clean(value) == "A A! AAA   JKL@!!!":
    print('OK')
else:
    ic(string_clean(value))
value = 'Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@'
if string_clean(value) == "Adgre Asad! AAA fvfdvJKL@":
    print('OK')
else:
    ic(string_clean(value))
value = 'Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 '
if string_clean(value) == "Addsadds A  $$sad! AAAe fKL@ ":
    print('OK')
else:
    ic(string_clean(value))
value = '33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 '
if string_clean(value) == "Addsadds A  $$sa!d! A!A!Ae$ f## ":
    print('OK')
else:
    ic(string_clean(value))
value = 'My "me3ssy" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?'
if string_clean(value) == "My \"messy\" data issues! Will they ever, ever be solved?":
    print('OK')
else:
    ic(string_clean(value))
value = 'Wh7y can\'t we3 bu1y the goo0d software3? #cheapskates3'
if string_clean(value) == "Why can't we buy the good software? #cheapskates":
    print('OK')
else:
    ic(string_clean(value))
