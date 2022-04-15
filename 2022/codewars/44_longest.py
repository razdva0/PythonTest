def longest(a1, a2):
    result = []
    for x in [a1, a2]:
        for z in x:
            if z not in result:
                result.append(z)
    return ''.join(sorted(result))
# return ''.join(sorted(set(a1 + s2)))


var_count, examples = "aretheyhere", "yestheyarehere"
if longest(var_count, examples) == "aehrsty":
    print('OK')
else: print(longest(var_count, examples))
var_count, examples = "loopingisfunbutdangerous", "lessdangerousthancoding"
if longest(var_count, examples) == "abcdefghilnoprstu":
    print('OK')
else: print(longest(var_count, examples))
var_count, examples = "inmanylanguages", "theresapairoffunctions"
if longest(var_count, examples) == "acefghilmnoprstuy":
    print('OK')
else: print(longest(var_count, examples))