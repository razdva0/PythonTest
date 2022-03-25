def series_sum(n):
	result = 0
	k = 1
	for x in range(n):
		result += 1 / k
		k += 3
	return f'{result:.2f}'


print(series_sum(5))
