import itertools
import sympy

def truncatable(prod):
	r = len(prod)
	if not sympy.isprime(int(prod)):
		return False
	for i in range(1,r):
		if not sympy.isprime(int(prod[:-i])):
			return False
		if not sympy.isprime(int(prod[i:])):
			return False
	return True

digitpossibilities = [[2,3,5,7],[2,3,5,7]]
truncatableprimes = set()

while len(truncatableprimes) < 11:
	prods = set(itertools.product(*digitpossibilities))
	for prod in prods:
		prod = "".join(map(str,prod))
		if truncatable(prod):
			truncatableprimes.add(int(prod))
	digitpossibilities.insert(1,[1,3,7,9])

print(sorted(truncatableprimes))
print(sum(truncatableprimes))