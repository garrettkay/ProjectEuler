import itertools

def generatesequence(digits):
	digitperms = itertools.permutations(digits)
	expressionset = set()
	for digitperm in digitperms:
		expressionset |= {(digitperm[0] + digitperm[1]) * (digitperm[2] + digitperm[3]),(digitperm[0] + digitperm[1]) * (digitperm[2] - digitperm[3]), (digitperm[0] - digitperm[1]) * (digitperm[2] - digitperm[3])}
		if (digitperm[0] + digitperm[1]) / (digitperm[2] + digitperm[3]).is_integer():
			expressionset.add(int(digitperm[0] + digitperm[1]) / (digitperm[2] + digitperm[3]))
		if (digitperm[0] + digitperm[1]) / (digitperm[2] - digitperm[3]).is_integer():
			expressionset.add(int(digitperm[0] + digitperm[1]) / (digitperm[2] - digitperm[3]))
		if (digitperm[0] - digitperm[1]) / (digitperm[2] - digitperm[3]).is_integer():
			expressionset.add(int(digitperm[0] - digitperm[1]) / (digitperm[2] - digitperm[3]))
		operationperms = itertools.product([1,2,3,4],repeat=3)
		for operationperm in operationperms:
			value = digitperm[0]
			index = 1
			for operation in operationperm:
				match operation:
					case 1:
						value += digitperm[index]
					case 2:
						value -= digitperm[index]
					case 3:
						value *= digitperm[index]
					case 4:
						value /= digitperm[index]
				index += 1
			if value.is_integer():
				expressionset.add(int(value))
	for i in range(1,1000000):
		if i not in expressionset:
			return i - 1

digitcombinations = list(itertools.combinations([1,2,3,4,5,6,7,8,9], 4))

maxseq = 0
maxcombo = (0,0,0,0)
for digitcombination in digitcombinations:
	sequence = generatesequence(digitcombination)
	if sequence > maxseq:
		maxseq = sequence
		maxcombo = digitcombination

print(maxcombo,maxseq)