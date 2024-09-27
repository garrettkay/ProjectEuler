import itertools
import sympy

circularprimes = set([2,5])
primes = set()

for r in range(1,7):
	prods = set(itertools.product([1,3,7,9],repeat = r))
	for prod in prods:
		prodstring = "".join(map(str,prod))
		if sympy.isprime(int(prodstring)):
			primes.add(prodstring)

primescopy = primes.copy()
for prime in primescopy:
	cycles = set()
	for i in range(len(prime)):
		cycles.add(prime[i:] + prime[:i])
	if primes >= cycles:
		circularprimes.update(map(int,cycles))
		primes.difference_update(cycles)
	else:
		primes.difference_update(cycles)

print(sorted(circularprimes))
print(len(circularprimes))