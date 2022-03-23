a, b = map(int, input().split())
old_a = a
old_b = b
while a != b:
	if a > b:
		b += old_b
	if b > a:
		a += old_a
print(a)
