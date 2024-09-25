import math

count = 0
for n in range(1,101):
	for r in range(n//2 + 1):
		if math.comb(n,r) > 1000000:
			count += n + 1 - (2 * r)
			break
print(count)