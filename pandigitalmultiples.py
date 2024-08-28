import itertools

perms = itertools.permutations([9,8,7,6,5,4,3,2,1])
pandigitalmultiples = []

for i in range(9000,10000):
	if set(map(int,str(i))).union(set(map(int,str(i * 2)))) == set([1,2,3,4,5,6,7,8,9]):
		pandigitalmultiples.append(i * 100000 + i * 2)

print(pandigitalmultiples)