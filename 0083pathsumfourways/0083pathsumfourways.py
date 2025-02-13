edges = []
with open("0083pathsumfourways\\0083_matrix.txt", 'r') as file:
	for line in file:
		edges.append(list(map(int, line.split(","))))

paths = [[10**10 for _ in range(80)] for _ in range(80)]
paths[0][0] = edges[0][0]

uvcells = set()
for i in range(80):
	for j in range(80):
		uvcells.add((i,j))

while uvcells:
	minuvcell = 10**10
	x = 81
	y = 81
	for i in range(80):
		for j in range(80):
			if (i,j) in uvcells and paths[i][j] < minuvcell:
				minuvcell = paths[i][j]
				x,y = i,j
	uvcells.remove((x,y))
	try:
		if (x + 1,y) in uvcells:
			paths[x + 1][y] = min(paths[x + 1][y],paths[x][y] + edges[x + 1][y])
	except:
		pass
	try:
		if (x - 1,y) in uvcells:
			paths[x - 1][y] = min(paths[x - 1][y],paths[x][y] + edges[x - 1][y])
	except:
		pass
	try:
		if (x,y + 1) in uvcells:
			paths[x][y + 1] = min(paths[x][y + 1],paths[x][y] + edges[x][y + 1])
	except:
		pass
	try:
		if (x,y - 1) in uvcells:
			paths[x][y - 1] = min(paths[x][y - 1],paths[x][y] + edges[x][y - 1])
	except:
		pass

print(paths[-1][-1])