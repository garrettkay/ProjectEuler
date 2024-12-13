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

def expandfraction(contfrac):
	num = 1
	den = 0
	for value in contfrac.__reversed__():
		num,den = value*num + den,num
	return num,den

maxX = 0
maxY = 0
maxD = 0
for D in range(1,1001):
	contfrac = rootperiod(D)
	if contfrac[0] % 2 == 0:
		xyapprox = ([int(contfrac[1][0][:-1])] + contfrac[1][1:])[:-1]
	else:
		xyapprox = ([int(contfrac[1][0][:-1])] + 2 * contfrac[1][1:])[:-1]
	x,y = expandfraction(xyapprox)
	if x > maxX:
		maxX = x
		maxY = y
		maxD = D
print("Our max value of x satisfies the equation:",maxY,"** 2 *",maxD,"+ 1 =",maxX,"** 2")
print("x:",maxX,"y:",maxY,"D:",maxD)