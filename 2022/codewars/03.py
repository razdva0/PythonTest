def decipher_this(string):
	result = ''
	numbers = '0123456789'
	s = string.split()
	for x in s:
		first = ''
		second = ''
		last = ''
		for z in x:
			if z in numbers:
				first += z
			else:
				second += z
		i = 1
		if len(second) > 0:
			last += second[-1]
			while i < len(second) - 1:
				last += second[i]
				i += 1
			if len(second) > 1:
				last += second[0]
		if len(result) > 0:
			result += ' '
		result += chr(int(first)) + last
	return result


string = "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
print(decipher_this(string))
