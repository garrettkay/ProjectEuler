import math
import sympy

primefactors = dict()

def primefactorize(n):
	try:
		return primefactors[n]
	except:
		if sympy.isprime(n):
			primefactors[n] = [n]
			return [n]
		for i in range(2,math.isqrt(n) + 1):
			if n % i == 0:
				factors1 = primefactorize(i)
				factors2 = primefactorize(n//i)
				primefactors[n] = factors1 + factors2
				return factors1 + factors2

phi = dict()

for i in range(2,1000001):
	factors = primefactorize(i)
	seenfactors = set()
	product = 1
	if len(factors) == 1:
		phi[i] = i - 1
	else:
		product = 1
		for factor in factors:
			if factor in seenfactors:
				product *= factor
			else:
				seenfactors.add(factor)
				product *= phi[factor]
		phi[i] = product

print(sum(phi.values()))