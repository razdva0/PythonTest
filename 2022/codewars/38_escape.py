def escape(carpark):
    result = []
    ladder = 0
    down = 0
    you = -1
    for numx, x in enumerate(carpark):
        if 2 not in x and you < 0:
            continue
        you = ladder
        for numz, z in enumerate(x):
            if z == 2:
                you = numz
            if z == 1:
                ladder = numz
        if numx == len(carpark) - 1:
            ladder = len(x) - 1
        if you > ladder:
            if down > 0:
                result.append(f'D{down}')
                down = 0
            result.append(f'L{you - ladder}')
        elif you < ladder:
            if down > 0:
                result.append(f'D{down}')
                down = 0
            result.append(f'R{ladder - you}')
        elif down > 0 and numx == len(carpark) - 1:
            result.append(f'D{down}')
        down += 1
    return result


carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]
result = ["L4", "D1", "R4"]
if escape(carpark) == result:
    print('OK')
else:
    print(escape(carpark))

carpark = [[2, 0, 0, 1, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0]]
result = ["R3", "D2", "R1"]
if escape(carpark) == result:
    print('OK')
else:
    print(escape(carpark))

carpark = [[0, 2, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]
result = ["R3", "D3"]
if escape(carpark) == result:
    print('OK')
else:
    print(escape(carpark))

carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]
result = ["L4", "D1", "R4", "D1", "L4", "D1", "R4"]
if escape(carpark) == result:
    print('OK')
else:
    print(escape(carpark))

carpark = [[0, 0, 0, 0, 2]]
result = []
if escape(carpark) == result:
    print('OK')
else:
    print(escape(carpark))