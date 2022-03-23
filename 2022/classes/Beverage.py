prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
		  "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
		  "Pineapple": 3.5}


class Beverage:

	def __init__(self, ingredients):
		self.ingredients = ingredients

	def get_cost(self):
		cost = 0
		for x, y in prices.items():
			if x in self.ingredients:
				cost += y
		return str("$%.2f" % cost)
		#  return f'${cost:.2f}'

	def get_price(self):
		price = 0
		for x, y in prices.items():
			if x in self.ingredients:
				price += y
		return str("$%.2f" % (price * 2.5))

	def get_name(self):
		string = ''
		lst = sorted([x.replace('berries', 'berry') for x in self.ingredients])
		if len(lst) < 2:
			string += lst[0] + ' Smoothie'
		else:
			for x in lst:
				string += x
				string += ' '
			string += 'Fusion'
		return string


s1 = Beverage(['Strawberries', 'Banana', 'Apple'])
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())