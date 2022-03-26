def duplicate_encode(word):
    # word = word.lower()
    # counter = Counter(word)
    dct = {}
    for x in word.lower():
        if x in dct:
            dct[x] += 1
        else:
            dct[x] = 1
    return ''.join(['(' if dct[x] < 2 else ')' for x in word.lower()])
    # return ''.join(('(' if counter[c] == 1 else ')') for c in word)


print(duplicate_encode("din"))
if duplicate_encode("din") == "(((":
    print('OK')
else:
    print('-')
print(duplicate_encode("recede"))
if duplicate_encode("recede") == "()()()":
    print('OK')
else:
    print('-')
print(duplicate_encode("Success"))
if duplicate_encode("Success") == ")())())":
    print('OK')
else:
    print('-')
print(duplicate_encode("(( @"))
if duplicate_encode("(( @") == "))((":
    print('OK')
else:
    print('-')