def delete_nth(order, max_e):
    dct = {}
    result = []
    for x in order:
        if x in dct:
            dct[x] += 1
            if dct[x] <= max_e:
                result.append(x)
        else:
            dct[x] = 1
            result.append(x)
    print(result.count(1))
    return result


assert delete_nth([20, 37, 20, 21], 1) == [20, 37, 21]
assert delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]


def delete_nthx(order, max_e):
    result = []
    for o in order:
        if result.count(o) < max_e:
            result.append(o)
    return result
