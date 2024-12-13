import math
import sympy

primefactors = dict()

def primefactorize(n):
	try:
		return primefactors[n]
	except:
		if sympy.isprime(n):
			primefactors[n] = {n}
			return {n}
		for i in range(2,math.isqrt(n) + 1):
			if n % i == 0:
				factors1 = primefactorize(i)
				factors2 = primefactorize(n//i)
				primefactors[n] = factors1.union(factors2)
				return factors1.union(factors2)

nphiratio = dict()
maxnphiratio = 0
maxn = 0
for i in range(2,1000001):
	factors = primefactorize(i)
	if len(factors) == 1:
		nphiratio[i] = i / (i - 1)
		if i / (i - 1) > maxnphiratio:
			maxnphiratio = i / (i - 1)
			maxn = i
	else:
		product = 1
		for factor in factors:
			product *= nphiratio[factor]
		nphiratio[i] = product
		if product > maxnphiratio:
			maxnphiratio = product
			maxn = i

print("n =",maxn,"n / phi =",maxnphiratio)