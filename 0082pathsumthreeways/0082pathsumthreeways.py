matrix = []
with open("0082pathsumthreeways\\0082_matrix.txt", 'r') as file:
	for line in file:
		matrix.append(list(map(int, line.split(","))))
matrix = list(map(list, zip(*matrix)))

def pathvalue(a,b):
	sum = matrix[-1][b]
	for index in range(min(a,b),max(a,b) + 1):
		sum += matrix[-2][index]
	return sum

while len(matrix) > 1:
	tempvalues = []
	for i in range(len(matrix[0])):
		minpath = 1000000
		for j in range(len(matrix[0])):
			pv = pathvalue(i,j)
			if pv < minpath:
				minpath = pv
		tempvalues.append(minpath)
	matrix = matrix[:-2] + [tempvalues]

print(min(matrix[0]))