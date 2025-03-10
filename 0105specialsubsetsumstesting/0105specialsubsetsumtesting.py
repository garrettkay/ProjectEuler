import itertools

with open('0105specialsubsetsumstesting\\0105_sets.txt', 'r') as file:
	specialsets = [list(map(int, line.strip().split(','))) for line in file]

def isspecialsumset(specialset):
	specialset = sorted(specialset)
	for i in range(1,len(specialset) + 1 // 2):
		if sum(specialset[:i + 1]) <= sum(specialset[-i:]):
			return False
	sums = set()
	for j in range(len(specialset)):
		for subset in itertools.combinations(specialset,j + 1):
			subsetsum = sum(subset)
			if subsetsum in sums:
				return False
			else:
				sums.add(subsetsum)
	return True

total = 0
for specialset in specialsets:
	if isspecialsumset(specialset):
		total += sum(specialset)
print(total)