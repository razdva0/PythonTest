ages = [14, 18, 21, 16, 19]
is_adult = lambda age: age >= 18
list_adult = list(filter(is_adult, ages))
print(list_adult)
is_adult = lambda age: age - 18
list_adult = list(filter(is_adult, ages))
print(list_adult)
