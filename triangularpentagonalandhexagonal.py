import math

trinum = lambda n: int((n * (n + 1)) / 2)

def ispentagonal(n):
	return ((1 + math.sqrt(1 + 24 * n)) / 6).is_integer()

def ishexagonal(n):
	return ((1 + math.sqrt(1 + 8 * n)) / 4).is_integer()

for i in range(1,1000000):
	tri = trinum(i)
	if ispentagonal(tri) and ishexagonal(tri):
		print(tri)