class Pizza:
	order_number = 0

	def __init__(self, ingredients):
		self.ingredients = ingredients
		Pizza.order_number += 1
		self.order_number = Pizza.order_number

	@classmethod
	def hawaiian(cls):
		return cls(['ham', 'pineapple'])

	@classmethod
	def meat_festival(cls):
		return cls(['beef', 'meatball', 'bacon'])

	@classmethod
	def garden_feast(cls):
		return cls(['spinach', 'olives', 'mushroom'])


p1 = Pizza(['bacon', 'parmesan', 'ham'])
p2 = Pizza.hawaiian()
print(p1.ingredients)
print(p2.ingredients)
print(p1.order_number)
print(p2.order_number)
