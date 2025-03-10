import itertools

def isspecialsumset(specialset):
	for i in range(1,len(specialset) // 2):
		if sum(specialset[:i + 1]) < sum(specialset[-i:]):
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

bestspecialsum = 1000
bestspecialsumset = []
for i in range(25):
	testset = [i,i + 11,i + 18,i + 19,i + 20,i + 22,i + 25]
	if sum(testset) > bestspecialsum:
		continue
	if isspecialsumset(testset):
		bestspecialsum = sum(testset)
		bestspecialsumset = testset

print(bestspecialsumset,bestspecialsum)