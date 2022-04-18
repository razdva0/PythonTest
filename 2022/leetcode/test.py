l1 = [1, 2, 3]
l2 = [1, 2, 3, 4, 5, 6]

for num, x in enumerate(l2):
    if num >= len(l1):
        l1.append(0)
print(l1)