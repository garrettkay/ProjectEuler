import math

def rootperiod(n):
	frac = [str(math.isqrt(n)) + ";"]
	num = 1
	rem = -math.isqrt(n)
	if math.sqrt(n).is_integer():
		return (0,frac)
	while True:
		nextfracterm = int(num * (math.sqrt(n) - rem) / (n - rem ** 2))
		frac.append(nextfracterm)
		num, rem = int((n - rem ** 2)/num), int((num * -rem - nextfracterm * (n - rem ** 2)) / num)
		if num == 1 and rem == -math.isqrt(n):
			break
	return (len(frac) - 1,frac)

count = 0
for n in range(1,10001):
	perfrac = rootperiod(n)
	if perfrac[0] % 2 == 1:
		count += 1
print(count)