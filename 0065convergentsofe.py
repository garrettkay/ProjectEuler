def convergence(frac):
	num = 0
	den = 1
	for i in range(len(frac)):
		num, den = den, frac[-1-i] * den + num
	return den,num

frac = []
for i in range(1,34):
	frac.extend([1,1,2 * i])
frac[0] += 1
frac.append(1)

approx = convergence(frac)

print(approx)
print(approx[0]/approx[1])
print(sum(map(int,str(approx[0]))))