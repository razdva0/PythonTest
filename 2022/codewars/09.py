def encode(st):
	string = ""
	for x in st:
		if x == 'a':
			string += '1'
		elif x == 'e':
			string += '2'
		elif x == 'i':
			string += '3'
		elif x == 'o':
			string += '4'
		elif x == 'u':
			string += '5'
		else:
			string += x
	return string


def decode(st):
	string = ""
	for x in st:
		if x == '1':
			string += 'a'
		elif x == '2':
			string += 'e'
		elif x == '3':
			string += 'i'
		elif x == '4':
			string += 'o'
		elif x == '5':
			string += 'u'
		else:
			string += x
	return string


def encodex(s, t=str.maketrans("aeiou", "12345")):
	return s.translate(t)


def decodex(s, t=str.maketrans("12345", "aeiou")):
	return s.translate(t)


def encodey(st):
	L = []
	A = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
	for i in st:
		if i in A:
			L.append(A[i])
		else:
			L.append(i)
	return "".join(L)


def decodey(st):
	L = []
	A = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}
	for i in st:
		if i in A:
			L.append(A[i])
		else:
			L.append(i)
	return "".join(L)


print(encodex("Hello, world"))
