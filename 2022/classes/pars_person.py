class Employee():

	def __init__(self, name, lname, gold):
		self.first_name = name
		self.last_name = lname
		self.salary = gold

	@classmethod
	def from_string(cls, string):
		s = string.split('-')
		return cls(s[0], s[1], int(s[2]))


emp1 = Employee('Vasya', 'Mironov', 6000)
emp2 = Employee.from_string('Vasyax-Mironovx-5000')
print(emp1.first_name)
print(emp1.salary)
print(emp2.first_name)
print(emp2.salary)
