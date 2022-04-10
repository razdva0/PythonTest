import itertools as it

iterable = [1, 2, 3]

iterator = iter(iterable)
print(type(iterator))
even_number = [x for x in range(10) if x % 2 == 0]
print(even_number)
even_number = it.count(0, 2)
print(list(next(even_number) for _ in range(5)))
print(list(zip(it.count(), ['a', 'b', 'c'])))


def print_iterable(iterable, end = None):
    for x in iterable:
        if end:
            print(x, end=end)
        else:
            print(x)


ones = it.repeat(1, 5)
print_iterable(ones, ' ')
print('')
pos_neg_ones = it.cycle([1, -1])
print(list(next(pos_neg_ones) for _ in range(10)))

letters = it.cycle(['A', 'B', 'C'])
print(list(next(letters) for _ in range(10)))

print('it.accumulate', list(it.accumulate([1, 2, 3, 4, 5])))
print('it.accumulate', list(it.accumulate(['A', 'B', 'C', 'D'])))
print('it.accumulate', list(it.accumulate([3, 1, 4, 2, 7, 3, 8, 5, 9], max)))
print('it.chain', list(it.chain('ABC', 'DEF')))
print('it.chain', list(it.chain.from_iterable(['ABC', 'DEF'])))
print('it.dropwhile', list(it.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5])))
print([x for x in range(1, 6) if x >= 3])
print('it.takewhile', list(it.takewhile(lambda x: x < 3, range(1, 6))))
print('it.filterfalse', list(it.filterfalse(lambda x: x % 2 == 0, range(10))))
iterable = iter([1, 2, 3])
print_iterable(iterable, ' ')
print('\niterable is exhausted')
print_iterable(iterable, ' ')
print('')
iterable1, iterable2 = it.tee([1, 2, 3], 2)
print_iterable(iterable1, ' ')
print('\niterable is exhausted')
print_iterable(iterable2, ' ')
print('')
names = ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding']
ratings = [2842, 2822, 2801]

for name, rating in zip(names, ratings):
    print(f'{name}:{rating}')

players = dict(zip(names, ratings))
print(players)
players = dict(it.zip_longest(names, ratings, fillvalue=0))
print(players)

for key, grp in it.groupby([1, 1, 1, 2, 2, 3, 2, 3, 3]):
    print('{}:{}'.format(key, list(grp)))


for key, grp in it.groupby(sorted([1, 1, 1, 2, 2, 3, 2, 3, 3])):
    print('{}:{}'.format(key, list(grp)))

forecast = [{'humidity': 20, 'temperature': 78, 'wind': 12},
            {'humidity': 50, 'temperature': 61, 'wind': 10},
            {'humidity': 100, 'temperature': 81, 'wind': 5},
            {'humidity': 90, 'temperature': 63, 'wind': 15}]


def group_sorted(iterable, key=None):
    return it.groupby(sorted(iterable, key=key), key=key)


group_data = group_sorted(forecast, key=lambda x: x['humidity'])
for key, grp in group_data:
    print('{}:{}'.format(key, list(grp)))

even_number = it.count(0, 2)
print([x for x in range(20) if x % 2 == 0])

print('it.islice', list(it.islice(even_number, 0, 10, 1)))

pin = [2, 4, 6]
print('it.permutations', list(it.permutations(pin)))

ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']
lst = list(it.product(ranks, suits))
print('it.product', lst)
