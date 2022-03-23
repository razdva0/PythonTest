def any_duplicates(square):
	my_list = []  # my_list = [i for x in square for i in x]
	for x in square:
		for i in x:
			my_list.append(i)
	i = 0
	while i < len(my_list):
		j = i + 1
		while j < len(my_list):
			if my_list[i] == my_list[j]:
				return True
			j += 1
		i += 1
	return False
#any_duplicates([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(any_duplicates([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
