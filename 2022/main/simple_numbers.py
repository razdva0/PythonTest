from time import time as t

n = int(input("n = "))
st = t()
a = list(range(n+1))
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
et = t()
print(et - st)
print(lst)
