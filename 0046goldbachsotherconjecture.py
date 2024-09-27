import sympy
import math

def primesquaredecom(n):
	if sympy.isprime(n):
		print(str(n) + " is decomposed as prime " + str(n))
		return True
	for i in range(1,math.isqrt(n) + 1):
		if sympy.isprime(n - 2 * i ** 2):
			print(str(n) + " is decomposed as prime " + str(n - 2 * i ** 2) + " and square " + str(i ** 2))
			return True
	return False

for i in range(1,10000):
	if not primesquaredecom(2 * i + 1):
		print(2 * i + 1)
		break