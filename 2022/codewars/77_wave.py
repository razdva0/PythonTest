def wave(people):
    return [''.join([people[z].upper() if z == x else people[z] for z in range(len(people))]) for x in range(len(people)) if people[x].isalpha()]
    # return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]


result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
if wave("hello") == result:
    print('OK')

result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
if wave("two words") == result:
    print('OK')