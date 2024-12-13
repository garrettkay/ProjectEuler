import sympy

primecount = 0

for i in range(3,100001,2):
	if sympy.isprime(i ** 2 - (i - 1)):
		primecount += 1
	if sympy.isprime(i ** 2 - 2 * (i - 1)):
		primecount += 1
	if sympy.isprime(i ** 2 - 3 * (i - 1)):
		primecount += 1
	if primecount / (2 * (i - 1) + 1) < 0.1:
		print("side length of",i,"gives",primecount,"/",(2 * (i - 1) + 1),"primes on the diagonal")
		break