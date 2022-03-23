while True:
	s = int(input("Введите количество палочек: "))
	while s > 0:
		k = 0
		while k < 1 or k > 3:
			k = int(input(f'Первый игрок, ваш ход, осталось {s} палочек\n'))
		s -= k
		if s == 1:
			print("Выиграл первый игрок")
			break
		elif s < 1:
			print("Выиграл второй игрок")
			break
		k = 0
		while k < 1 or k > 3:
			k = int(input(f'Второй игрок, ваш ход, осталось {s} палочек\n'))
		s -= k
		if s == 1:
			print("Выиграл второй игрок")
			break
		elif s < 1:
			print("Выиграл первый игрок")
			break
