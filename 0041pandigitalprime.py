import itertools
import sympy

for i in range(1,10):
	perms = itertools.permutations(range(i,0,-1))
	for perm in perms:
		if sympy.isprime(int("".join(map(str,perm)))):
			print("".join(map(str,perm)) + " is the largest " + str(i) + " digit pandigital prime")
			break