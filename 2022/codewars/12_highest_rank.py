def highest_rank(arr):
    dct = {}
    for x in arr:
        if x in dct:
            dct[x] += 1
        else:
            dct[x] = 1
    lst = [x for x, y in dct.items() if y == max(dct.values())]
    return max(lst)


print(highest_rank([172, 38, 205, 49, 94, 251, 89, 49, 105, 236, 174, 140, 198, 86, 160]))
