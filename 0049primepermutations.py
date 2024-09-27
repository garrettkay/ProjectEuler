import sympy

for i in range(1000,10000):
	if not sympy.isprime(i):
		continue
	for j in range(1,(10000-i)//2):
		p1 = i
		p2 = i + j
		p3 = i + 2 * j
		if not sympy.isprime(p2):
			continue
		if not sympy.isprime(p3):
			continue
		digits1 = sorted(list(map(int,str(p1))))
		digits2 = sorted(list(map(int,str(p2))))
		digits3 = sorted(list(map(int,str(p3))))
		if digits1 != digits2 or digits1 != digits3:
			continue
		print(p1,p2,p3)