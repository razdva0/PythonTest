from collections import Counter

mass = ['Vasya', 'Petya', 'Vasya', 'Nurken', 'Nurken', 'Vasya', 55, 55]
counter = Counter(mass)
for c in counter:
    print(c, counter[c])
