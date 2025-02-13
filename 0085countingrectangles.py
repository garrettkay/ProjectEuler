rectcount = lambda x,y: (x * (x + 1) * y * (y + 1)) // 4


close = 2000000
bestapprox = (1,1)
for a in range(1000):
	for b in range(a):
		count = rectcount(a,b)
		if abs(2000000 - count) < close:
			close = abs(2000000 - count)
			bestapprox = (a,b)

print(bestapprox)
print(rectcount(bestapprox[0],bestapprox[1]))