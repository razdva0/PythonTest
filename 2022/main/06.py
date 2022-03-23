s = input()
t1 = input()
t2 = input()


def ft_upper(t3, k):
	up = t3.upper()
	return up[k]


def ft_c(s1, t):
	i = 0
	c = ""
	for x in s1:
		if i < len(t):
			if x == t[i]:
				c += ft_upper(t, i)
				i += 1
			else:
				c += x
		else:
			c += x
	return c


def ft_search(c3):
	j = ""
	k = 0
	for x in c3:
		if x.isupper() and j.islower():
			k += 1
		elif x.islower() and j.isupper():
			k += 1
		j = x
	return k


c1 = ft_c(s, t1)
c2 = ft_c(s, t2)
k1 = ft_search(c1)
k2 = ft_search(c2)

print(min(k1, k2))
