import itertools

permutations = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))
pdp = set()

print(permutations)
for perm in permutations:
	f1, f2, prod = perm[0], perm[1] * 1000 + perm[2] * 100 + perm[3] * 10 + perm[4], perm[5] * 1000 + perm[6] * 100 + perm[7] * 10 + perm[8]
	if f1 * f2 == prod:
		print(str(f1) + " * " + str(f2) + " = " + str(prod))
		pdp.add(prod)
	f1, f2, prod = perm[0] * 10 + perm[1], perm[2] * 100 + perm[3] * 10 + perm[4], perm[5] * 1000 + perm[6] * 100 + perm[7] * 10 + perm[8]
	if f1 * f2 == prod:
		print(str(f1) + " * " + str(f2) + " = " + str(prod))
		pdp.add(prod)

print(pdp)

sum = 0 
for prod in pdp:
	sum += prod

print(sum)