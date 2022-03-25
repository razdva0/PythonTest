def ft_swap(string):
    result = ''
    for x in string:
        result = x + result
    return result


def reverse_alternate(string):
    result = []
    i = 0
    for x in string.split():
        if i % 2 == 1:
            result.append(ft_swap(x))
        else:
            result.append(x)
        i += 1
    return " ".join(result)


print(reverse_alternate("Did it work?"))
if "Did ti work?" == reverse_alternate("Did it work?"):
    print('OK')
else:
    print('KO')