import collections

ptriples = collections.defaultdict(set)

for m in range(2,867):
	for n in range(1,m):
		a,b,c,l = m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2, 2 * m * (m + n)
		if l > 1500000:
			break
		for i in range(1,125001):
			if i * l > 1500000:
				break
			ptriples[i * l].add((min(i * a, i * b), max(i * a, i * b), i * c))

print(sum(len(elements) == 1 for elements in ptriples.values()))