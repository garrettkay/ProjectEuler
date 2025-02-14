sum = 0
for m in range(2,31623):
	for n in range(1,m):
		a,b,c = m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2
		if c > 333333333:
			break
		if (c - 1) / 2 == a or (c - 1) / 2 == b:
			sum += 3 * c - 1
		if (c + 1) / 2 == a or (c + 1) / 2 == b:
			sum += 3 * c + 1

print(sum)