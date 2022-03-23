s = list(map(str, input().split()))
i = 0
a = 0
b = 0
while i < len(s[0]):
	j = 0
	while j < len(s[1]):
		if s[0][i] == s[1][j]:
			a += 1
			if i == j:
				b += 1
		j += 1
	i += 1
print(b, a - b)
