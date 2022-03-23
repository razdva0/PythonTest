class Name():

	def __init__(self, first_name, last_name):
		self.first_name = first_name.capitalize()
		self.last_name = last_name.capitalize()
		self.full_name = self.first_name + ' ' + self.last_name
		self.initials = self.first_name[0] + '.' + self.last_name[0]

	def first_name(self):
		return self.first_name

	def last_name(self):
		return self.last_name

	def full_name(self):
		return self.first_name

	def initials(self):
		return self.initials


name = Name('vasily', 'mironov')
print(name.first_name)
print(name.last_name)
print(name.full_name)
print(name.initials)