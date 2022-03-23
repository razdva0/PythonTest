def find_it(seq):
	for i in seq:
		if seq.count(i) % 2 != 0:
			return i
	return -1


seqx = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]
print(find_it(seqx))
