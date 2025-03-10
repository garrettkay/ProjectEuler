import math
import itertools

def subsettests(n):
	count = 0
	for i in range(2,n // 2 + 1):
		count += math.comb(n,i * 2) * splitsubsets(i * 2)
	return count

def splitsubsets(n):
	count = 0
	for comb in itertools.combinations(range(1,n + 1),n // 2):
		set1 = set(comb)
		set2 = set(range(1,n + 1)) - set1
		set1larger = False
		set2larger = False
		while set1:
			if max(set1) > max(set2):
				if set2larger:
					count += 1
					break
				else:
					set1larger = True
			else:
				if set1larger:
					count += 1
					break
				else:
					set2larger = True
			set1.remove(max(set1))
			set2.remove(max(set2))
	return count // 2

print(subsettests(12))