import random
import itertools

'''
def randoms(min, max, n):
    return [random.randint(min, max) for _ in range(n)]


for r in randoms(10, 30, 5):
    print(r)
'''


def randoms(min, max):
    while True:
        yield random.randint(min, max)


rand = randoms(1, 10)
five_rand = list(itertools.islice(rand, 6))
print(five_rand)


def read_line_by_line(file):
    """Lazy function (generator0 to read file line by line"""
    while True:
        line = file.readline()
        if not line:
            break
        yield line


'''
file = open('C:\Programming\JavaCore\Java\src\Main.java')
for line in read_line_by_line(file):
    print(line.rstrip())'''

my_list = [1, 2, 3, 4]
squares = (x ** 2 for x in my_list)
for x in squares:
    print(x)
