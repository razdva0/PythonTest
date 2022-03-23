n = int(input())
i = 0
for x in range(n):
	n_list = list(map(int, input().split()))
	while x < n:
		if n_list[x] == 1:
			i += 1
		x += 1
print(i)