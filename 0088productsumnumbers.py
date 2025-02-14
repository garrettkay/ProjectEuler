import sympy
import time

t1 = time.time()

def genfactorizations(n):
	factorizations = set()
	stack = [(n, [])]
	while stack:
		current, path = stack.pop()
		for divisor in sympy.divisors(current):
			quotient = current // divisor
			if divisor != 1 and quotient != 1:
				newpath = sorted(path + [divisor, quotient])
				factorizations.add(tuple(newpath))
				if quotient != 1 and quotient != divisor:
					stack.append((quotient, path + [divisor]))
	return factorizations

kset = set(range(2,12001))
minprodsumnums = set()

i = 0
while kset:
	i += 1
	for factorization in genfactorizations(i):
		k = i + len(factorization) - sum(factorization)
		if k in kset:
			minprodsumnums.add(i)
			kset.remove(k)

print(sum(minprodsumnums))

print(time.time() - t1)