import itertools

distinctarrangements = set()

squares = [(0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(1,8)]

def iscompatible(die1,die2):
	d1 = list(die1)
	d2 = list(die2)
	if 9 in d1:
		d1[d1.index(9)] = 6
	if 9 in d2:
		d2[d2.index(9)] = 6
	for square in squares:
		if not(square[0] in d1 and square[1] in d2 or square[1] in d1 and square[0] in d2):
			return False
	return True

dice = list(itertools.combinations([0,1,2,3,4,5,6,7,8,9],6))

count = 0
for i in range(len(dice)):
	for j in range(i):
		if iscompatible(dice[i],dice[j]):
			count += 1
print(count)