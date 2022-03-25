class Caracter(object):

	_instance = None

	def __new__(cls):
		if not cls._instance:
			cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self):
		self.race = 'Elf'


class Caracter2(object):

	def __init__(self):
		self.race = 'Elf'


c1 = Caracter()
c2 = Caracter2()
d1 = Caracter()
d2 = Caracter2()
d1.race = 'Ork'
d2.race = 'Human'
print(c1.race)
print(c2.race)
print(d1.race)
print(d2.race)
