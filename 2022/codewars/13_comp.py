def comp(array1, array2):
    try:
        lst = sorted([x * x for x in array1])
        array2 = sorted(array2)
        i = 0
        while i < len(array2):
            if not array2[i] == lst[i]:
                return False
            i += 1
        return True
    except:
        return False


a = [-121, -144, 19, -161, 19, -144, 19, -11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a, b))


def compx(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False