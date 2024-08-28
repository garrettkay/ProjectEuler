import itertools

permutations = itertools.permutations([1,2,3,4,5,6,7,8,9],3)
dcf = []

for perm in permutations:
	if perm[0] > perm[1]:
		continue
	if perm[0]/perm[1] == (perm[0] * 10 + perm[2])/(perm[1] * 10 + perm[2]):
		dcf.append((perm[0] * 10 + perm[2],perm[1] * 10 + perm[2]))
	if perm[0]/perm[1] == (perm[2] * 10 + perm[0])/(perm[1] * 10 + perm[2]):
		dcf.append((perm[2] * 10 + perm[0],perm[1] * 10 + perm[2]))
	if perm[0]/perm[1] == (perm[0] * 10 + perm[2])/(perm[2] * 10 + perm[1]):
		dcf.append((perm[0] * 10 + perm[2],perm[2] * 10 + perm[1]))
	if perm[0]/perm[1] == (perm[2] * 10 + perm[0])/(perm[2] * 10 + perm[1]):
		dcf.append((perm[2] * 10 + perm[0],perm[2] * 10 + perm[1]))

print(dcf)