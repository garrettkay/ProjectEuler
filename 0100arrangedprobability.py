a = 15
b = 21

while b < 10**12:
	a,b = 3 * a + 2 * b - 2, 4 * a + 3 * b - 3

print(a,b)