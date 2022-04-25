def spiralize(size):
    result = list(map(lambda x: list(map(lambda y: 1 if (int(size + 1) / 2) % 2 == 1 else 0, range(0, size))),
                      range(0, size)))
    spiral = 1
    for i in range(0, int(size / 2)):
        for u in range(0, size - i * 2):
            result[i][u + i] = spiral
            result[u + i][i] = spiral
            result[size - i - 1][u + i] = spiral
            result[u + i][size - i - 1] = spiral

            if size % 4 == 0:
                if i != int(size / 2) - 1:
                    result[i + 1][i] = 1 - spiral
            else:
                result[i + 1][i] = 1 - spiral
        spiral = 1 - spiral
    return result


if spiralize(5) == [[1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1],
                    [1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1]]:
    print('OK')
else:
    for x in spiralize(5):
        print(x)
if spiralize(8) == [[1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 1, 0, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]]:
    print('OK')
else:
    for x in spiralize(8):
        print(x)


def spiralizex(size):
    # Make a snake
    spiral = [[1 - min(i,j,size-max(i,j)-1)%2 for j in xrange(size)] for i in xrange(size)]
    for i in xrange(size/2-(size%4==0)):
      spiral[i+1][i] = 1 - spiral[i+1][i]
    return spiral
