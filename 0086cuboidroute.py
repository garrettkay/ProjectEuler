import collections
import math

integerpaths = collections.defaultdict(int)

for m in range(2,500):
	for n in range(1,m):
		if (m - n) % 2 == 0 or math.gcd(m,n) != 1:
			continue
		a,b = m ** 2 - n ** 2, 2 * m * n
		for i in range(1,5000):
			if min(a,b) * i > 5000:
				break
			integerpaths[max(a,b) * i] += (min(a,b) * i) // 2
			integerpaths[min(a,b) * i] += max(0,(min(a,b) * i) + 1 + (-i * max(a,b)) // 2)

sum = 0
for i in range(1000000):
	sum += integerpaths[i]
	if sum > 1000000:
		print(i,sum)
		break