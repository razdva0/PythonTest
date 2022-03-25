def smallest(n):
	num = str(n)
	result = [n, len(num), 0]
	i = 0
	while i < len(num):
		j = 0
		while j < len(num):
			string = ''
			k = 0
			while k < len(num):
				if k == i and k != j:
					k += 1
					continue
				if k == j and k < i:
					string += num[i]
				string += num[k]
				if k == j and k > i:
					string += num[i]
				k += 1
			if int(string) < result[0]:
				result[0] = int(string)
				result[1] = i
				result[2] = j
			j += 1
		i += 1
	return result


print(smallest(261235))
