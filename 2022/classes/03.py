import math


class Shape():

	def __init__(self):
		print('Sape created')

	def draw(self):
		print('Drawing a shape')

	def area(self):
		print('Calc area')

	def perimeter(self):
		print('Calc perimeter')


shape = Shape()


class Rectangle(Shape):

	def __init__(self, width, height):
		Shape.__init__(self)

		self.width = width
		self.height = height

		print('Rectangle created')

		Shape.area(self)

	def area(self):
		return self.width * self.height

	def perimeter(self):
		return 2 * (self.width + self.height)

	def draw(self):
		print(f'Drawing rectangle with width = {self.width} and height = {self.height}')


rect = Rectangle(10, 15)
print(rect.area())
print(rect.perimeter())
rect.draw()


class Triangle(Shape):

	def __init__(self, a, b, c):
		Shape.__init__(self)

		self.a = a
		self.b = b
		self.c = c

		print('Triangle created')

	def draw(self):
		print(f'Drawing triangle with sides = {self.a}, {self.b}, {self.c}')

	def area(self):
		s = (self.a + self.b + self.c) / 2
		return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

	def perimeter(self):
		return self.a + self.b + self.c


triangle = Triangle(10, 10, 10)
triangle.draw()
print(triangle.area())
print(triangle.perimeter())

for shape in [rect, triangle]:
	shape.draw()