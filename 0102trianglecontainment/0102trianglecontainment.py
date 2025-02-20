import numpy as np

tris = np.loadtxt('0102trianglecontainment\\0102_triangles.txt',delimiter=',',dtype=int)

count = 0
for tri in tris:
	area = abs((tri[2] - tri[0]) * (tri[5] - tri[1]) - (tri[3] - tri[1]) * (tri[4] - tri[0]))
	if area == (abs((tri[0] * tri[3]) - (tri[1] * tri[2])) + abs((tri[0] * tri[5]) - (tri[1] * tri[4])) + abs((tri[2] * tri[5]) - (tri[3] * tri[4]))):
		count += 1

print(count)