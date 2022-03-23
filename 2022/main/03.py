s = []
i = 0
k = 0
while i < 10:
    s.append(int(input()))
    i += 1
for x in s:
    if x > i:
        k += 1

print(k)
