n, m, k = map(int, input().split())
a = list(map(int, input().split()))
s = []
c = []
x = 0
i = 0
j = 0
summ = 0
f = 0
while x < n:
	if a[x] == j and a[x] != m:
		if i == m:
			c.append(i)
			i = 0
		if i == 0:
			s.append(x)
		i += 1
	else:
		if i == m - 1:
			c.append(i + 1)
		i = 0
	j = a[x]
	x += 1
if i == m - 1:
	c.append(i + 1)
i = 0
while i < len(c):
	summ = a[s[i] - 1] * c[i]
	f += (c[i] * m - summ) / m
	i += 1
print(int(f))
p = len(c)
print(p)
i = 0
while i < len(c):
	print(s[i], c[i])
	i += 1
