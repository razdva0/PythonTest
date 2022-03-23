vasya = 'Vasya', 2
petya = 'Petya', 1


def hello_n(name: str, n: int):
	for i in range(n):
		print('Hello', name)


hello_n(*vasya)
hello_n(*petya)
print(vasya, *vasya)
