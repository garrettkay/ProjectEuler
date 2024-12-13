import math

minerror = 1
bestfrac = 0,0
for den in range(1000001):
	if den % 7 == 0:
		continue
	num = math.floor(3 * den / 7)
	if 3/7 - num/den < minerror:
		minerror = 3/7 - num/den
		bestfrac = num,den
print(bestfrac,minerror)