import itertools

perms = itertools.permutations([1,2,3,4,5,6,7,8,9])

magic5gons = []
for perm in perms:
	groups = [[perm[0],perm[4],perm[5]],[perm[1],perm[5],perm[6]],[perm[2],perm[6],perm[7]],[perm[3],perm[7],perm[8]],[10,perm[8],perm[4]]]
	if all(sum(group) == sum(groups[0]) for group in groups):
		magic5gons.append(sum(groups,[]))

sorted5gons = []
for gon in magic5gons:
	minhead = 11
	minloc = 0
	for i in range(5):
		if gon[i*3] < minhead:
			minhead = gon[i*3]
			minloc = i * 3
	sorted5gons.append(int("".join(map(str,gon[minloc:] + gon[:minloc]))))
print(sorted(sorted5gons))
print(max(sorted5gons))