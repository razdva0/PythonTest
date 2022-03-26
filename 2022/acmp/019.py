f = list(input().split())
a = 'ABCDEFGH'
b = '12345678'
steps = []
if f[0][0] in a and f[0][1] in b and len(f) == 2:
	for x in f[0]:
		if x in a:
			for q in b:
				steps.append(x + q)
		if x in b:
			for q in a:
				if q + x in steps:
					continue
				steps.append(q + x)
		
if f[1][0] in a and f[1][1] in b and len(f) == 2:
	for x in f[1]:
		if x in a:
			for q in b:
				steps.append(x + q)
		if x in b:
			for q in a:
				if q + x in steps:
					continue
				steps.append(q + x)
print(steps)
