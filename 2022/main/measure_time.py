from timeit import default_timer as timer
from functools import wraps  # @wraps(func)
import time  # time.sleep
import math  # math.factorial


def measure_time(func):
	@wraps(func)
	def inner(*args, **kwargs):
		start = timer()
		func(*args, **kwargs)
		end = timer()
		print(f'Function "{func.__name__}" took {end-start} for execution')
	return inner


@measure_time
def factorial(num):
	time.sleep(3)
	print(math.factorial(num))


factorial(10)
