import collections
import sympy
import heapq

summations = collections.defaultdict(set)

primes = []

for n in range(2,100):
	for p in primes:
		for summation in summations[n-p]:
			summations[n].add(tuple(heapq.merge(summation,(p,))))
	if sympy.isprime(n):
		summations[n].add((n,))
		primes.append(n)
	if len(summations[n]) > 5000 + sympy.isprime(n):
		print(n)
		break