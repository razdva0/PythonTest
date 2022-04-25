def dithering(width, height):
    size = 1
    while width > size or height > size:
        size *= 2
    if size == 1:
        yield 0, 0
    else:
        for (x, y) in dithering(size / 2, size / 2):
            for t in ((x, y), (x + size / 2, y + size / 2), (x + size / 2, y), (x, y+size/2)):
                if t[0] < width and t[1] < height:
                    yield t


print(list(dithering(3, 3)))
print(list(dithering(4, 4)))
print(list(dithering(6, 5)))
print(list(dithering(8, 8)))
print([i for i in range(1, 26) if i % 10 == 1])