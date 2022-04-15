def open_or_senior(data):
    return ['Senior' if x[0] >= 55 and x[1] > 7 else 'Open' for x in data]


if open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]) == ['Open', 'Senior', 'Open', 'Senior']:
    print('OK')
else: print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
if open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]) == ['Open', 'Open', 'Senior', 'Open']:
    print('OK')
else: print(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]))