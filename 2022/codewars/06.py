def filter_list(l):
	lst = []
	for x in l:
		if type(x) == int:
			lst.append(x)
	return lst
	#  return [x for x in l if type(x) is not str]


lst = [1, 2, 'lol', 'kek', 3]
print(filter_list(lst))
