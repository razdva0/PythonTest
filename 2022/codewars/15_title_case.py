def title_case(title, minor_words=''):
    result = []
    i = 0
    minor_words_lower = [x.lower() for x in minor_words.split()]
    for x in title.split():
        if x.lower in minor_words_lower and i > 0:
            result.append(x.lower())
        else:
            result.append(x.capitalize())
        i += 1
    return " ".join(result)


print(title_case('a clash of KINGS', 'a an the of'))
if title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings':
    print('OK')
else:
    print('KO')
