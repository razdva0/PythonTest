from abc import ABC
from abc import abstractmethod
import math


class Shape(ABC):

	def __init__(self):
		super().__init__()

	@abstractmethod
	def draw(self):
		pass

	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		print('calc perimeter')

	def drag(self):
		print('Basic dragging functionality')


class Triangle(Shape):

	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def draw(self):
		print(f'drawing a={self.a}, b={self.b}, c={self.c}')

	def area(self):
		s = (self.a + self.b + self.c) / 2
		return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

	def perimeter(self):
		super().perimeter()
		return self.a + self.b + self.c

	def drag(self):
		super().drag()
		print('Additional actions')


t = Triangle(10, 10, 10)
t.draw()
print(t.area())
print(t.perimeter())
t.drag()
