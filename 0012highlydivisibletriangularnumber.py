import math
import numpy
import sympy

tri = lambda x : (x * (x + 1)) // 2

'''
value = 0
while tri(value) < 250*250:
	value += 1
print(value)

# finding smallest triangular number greater than 250*250 (at value = 354)
'''

value = 350
while True:
	triangle = tri(value)
	if sympy.divisor_count(triangle) > 500:
		print(triangle)
		break
	value += 1