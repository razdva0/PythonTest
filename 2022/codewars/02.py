def data_reverse(data):
	result = []
	i = 0
	j = 0
	while i < len(data) / 8:
		s = []
		k = 0
		while k < 8:
			s.append(data[j])
			j += 1
			k += 1
		result = s + result
		i += 1
	return result


def data_reverse1(data):
	res = []

	for i in range(len(data) - 8, -1, -8):
		res.extend(data[i:i + 8])

	return res


def data_reverse2(data):
	data2 = []
	j = len(data)
	while j > 0:
		data2 = data2 + data[j-8:j]
		j = j - 8
	return data2


print(data_reverse([0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]))
#data_reverse([1, 2, 3, 4, 5])
