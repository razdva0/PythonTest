def dirReduc(arr):
    result = []
    for num, x in enumerate(arr):
        if len(result) == 0:
            result.append(x)
        elif x == 'NORTH' and result[-1] == 'SOUTH' or x == 'SOUTH' and result[-1] == 'NORTH':
            del result[-1]
        elif x == 'EAST' and result[-1] == 'WEST' or x == 'WEST' and result[-1] == 'EAST':
            del result[-1]
        else:
            result.append(x)
    return result


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
assert dirReduc(a) == ['WEST']
u = ["NORTH", "WEST", "SOUTH", "EAST"]
assert dirReduc(u) == ["NORTH", "WEST", "SOUTH", "EAST"]