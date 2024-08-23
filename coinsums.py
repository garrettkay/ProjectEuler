def tuplesum(a,b):
	tup = []
	for i in range(len(a)):
		tup.append(a[i] + b[i])
	return tuple(tup)

ways2p = set([(2,0,0,0,0,0,0,0),(0,1,0,0,0,0,0,0)])

ways5p = set([(0,0,1,0,0,0,0,0),(5,0,0,0,0,0,0,0)])

for way1 in ways2p:
	ways5p.add(tuplesum(way1,(3,0,0,0,0,0,0,0)))
	for way2 in ways2p:
		ways5p.add(tuplesum(way1,tuplesum(way2,(1,0,0,0,0,0,0,0))))

ways10p = set([(0,5,0,0,0,0,0,0),(0,0,0,1,0,0,0,0)])

for way1 in ways5p:
	for way2 in ways5p:
		ways10p.add(tuplesum(way1,way2))

ways20p = set([(0,0,0,0,1,0,0,0)])

for way1 in ways10p:
	for way2 in ways10p:
		ways20p.add(tuplesum(way1,way2))

ways50p = set([(0,0,0,0,0,1,0,0),(0,0,0,5,0,0,0,0)])

for way1 in ways20p:
	for way2 in ways20p:
		for way3 in ways10p:
			ways50p.add(tuplesum(way1,tuplesum(way2,way3)))

ways100p = set([(0,0,0,0,0,0,1,0),(0,0,0,0,5,0,0,0)])

for way1 in ways50p:
	for way2 in ways50p:
		ways100p.add(tuplesum(way1,way2))

ways200p = set([(0,0,0,0,0,0,0,1)])

for way1 in ways100p:
	for way2 in ways100p:
		ways200p.add(tuplesum(way1,way2))

print(len(ways200p))