def isrighttriangle(v1,v2):
	if v1 == (0,0) or v2 == (0,0) or v1 == v2:
		return False
	if v1[0] * v2[0] + v1[1] * v2[1] == 0:
		return True
	v3 = (v1[0] - v2[0], v1[1] - v2[1])
	if v1[0] * v3[0] + v1[1] * v3[1] == 0:
		return True
	if v2[0] * v3[0] + v2[1] * v3[1] == 0:
		return True
	return False

count = 0
for x1 in range(51):
	for y1 in range(51):
		for x2 in range(51):
			for y2 in range(51):
				if isrighttriangle((x1,y1),(x2,y2)):
					count += 1
print(count // 2)