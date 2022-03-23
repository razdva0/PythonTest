class Character():
	max_speed = 100
	dead_health = 0

	def __init__(self, race, damage=10, armor=20):
		self.race = race
		self.damage = damage
		self.armor = armor
		self.health = 100

	def hit(self, damage):
		self.health -= damage * (1 - self.armor / 100)

	def is_dead(self):
		return self.health == Character.dead_health


unit = Character("Elf")
print(type(unit))
print(f'Race: {unit.race}')
print(f'Damage {unit.race}: {unit.damage}')
print(f'Armor {unit.race}: {unit.armor}')
print(f'Health {unit.race}: {unit.health}')
damage = 20.0
unit.hit(damage)
print(f'{unit.race} took {damage} damage')
print(f'{unit.race} has {unit.health} health')
