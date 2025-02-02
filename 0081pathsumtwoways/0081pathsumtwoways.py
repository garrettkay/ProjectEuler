matrix = []
with open("0081pathsumtwoways\\0081_matrix.txt", 'r') as file:
	for line in file:
		matrix.append(list(map(int, line.split(","))))

maxvalue = 0
for line in matrix:
	for entry in line:
		if entry > maxvalue:
			maxvalue = entry

triangle = []
for i in range(len(matrix)):
	line = []
	for j in range(i + 1):
		line.append(matrix[j][i-j])
	triangle.append(line)
for k in range(len(matrix[0]) - 1):
	line = [maxvalue] * (k + 1)
	for l in range(79-k):
		line.append(matrix[k + l + 1][79-l])
	line += [maxvalue] * (k + 1)
	triangle.append(line)

while len(triangle) > 1:
	for i in range(len(triangle[-2])):
		triangle[-2][i] += min(triangle[-1][i],triangle[-1][i+1])
	triangle.pop(-1)
print(triangle[0][0])