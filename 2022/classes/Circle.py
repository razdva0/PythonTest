import math


class Circle():

	def __init__(self, radius):
		self.radius = radius

	def get_area(self):
		return math.pi * self.radius ** 2

	def get_perimeter(self):
		return math.pi * self.radius * 2


circle = Circle(4.44)
area = circle.get_area()
print(area)
perimeter = circle.get_perimeter()
print(perimeter)
