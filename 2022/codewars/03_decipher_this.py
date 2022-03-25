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


def encrypt_this(text):
	mass = text.split()
	result = ''
	for x in mass:
		if len(result) > 0:
			result += ' '
		i = 0
		while i < len(x):
			if i == 0:
				result += str(ord(x[i]))
			elif i == 1:
				result += x[-1]
			elif i == len(x) - 1:
				result += x[1]
			else:
				result += x[i]
			i += 1
	return result


string = "A wise old owl lived in an oak"
print(encrypt_this(string))
if "65 119esi 111dl 111lw 108dvei 105n 97n 111ka" == encrypt_this(string):
	print("OK")
else:
	print("KO")


def swapper(w):
	return w if len(w)<2 else w[-1] + w[1:-1] + w[0]


def encrypt_thisx(s):
	return ' '.join(w if not w else str(ord(w[0])) + swapper(w[1:]) for w in s.split())


def encrypt_thisxx(text):
	result = []
	for word in text.split():
		word = list(word)
		word[0] = str(ord(word[0]))
		if len(word) > 2:
			word[1], word[-1] = word[-1], word[1]
		result.append(''.join(word))
	return ' '.join(result)
