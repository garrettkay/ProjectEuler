import math

count = 0
for i in range(12001):
	for j in range(math.floor(i/3) + 1,math.ceil(i/2)):
		if math.gcd(i,j) == 1:
			count += 1

print(count)