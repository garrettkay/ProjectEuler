import sympy
import math

primefactors = dict()

def primefactorize(n):
	try:
		return primefactors[n]
	except:
		if sympy.isprime(n):
			primefactors.update({n:{n}})
			return {n}
		for i in range(2,math.isqrt(n) + 1):
			if n % i == 0:
				factors1 = primefactorize(i)
				factors2 = primefactorize(n//i)
				primefactors.update({n:factors1.union(factors2)})
				return factors1.union(factors2)

count = 0
for i in range(2,1000000):
	factors = primefactorize(i)
	if len(factors) == 4:
		count += 1
	else:
		count = 0
	if count == 4:
		print(i-3)
		print(i-2)
		print(i-1)
		print(i)
		break