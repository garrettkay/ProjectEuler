import math
import sympy

"""primefactors = dict()

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
nphiratiomin = 100
nmin = 0
for i in range(2,10**7):
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
				product *= phi[factor]
		phi[i] = product
		if sorted(map(int,str(i))) == sorted(map(int,str(product))):
			if i/phi[i] < nphiratiomin:
				nphiratiomin = i/phi[i]
				nmin = i
print(nmin,phi[nmin],nphiratiomin)"""

primes = list(sympy.primerange(5000))

phimin = 100
nmin = 0
for p in range(len(primes)):
	for q in range(p,len(primes)):
		phi = (primes[p] - 1) * (primes[q] - 1)
		n = primes[p] * primes[q]
		if n > 10**7:
			break
		if sorted(map(int,str(n))) == sorted(map(int,str(phi))):
			if n/phi < phimin:
				phimin = n/phi
				nmin = n
print(nmin,phimin,nmin/phimin)