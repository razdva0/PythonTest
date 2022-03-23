def two_sum(numbers, target):
	x = 0
	while x < len(numbers):
		y = x
		while y < len(numbers):
			if numbers[x] + numbers[y] == target and x != y:
				return (x, y)
			y += 1
		x += 1
	return []
#  	def two_sum(nums, t):
#  		for i, x in enumerate(nums):
#  			for j, y in enumerate(nums):
#  				if i != j and x + y == t:
#  		return [i, j]

print(two_sum([0, 1, 2, 3], 4))
