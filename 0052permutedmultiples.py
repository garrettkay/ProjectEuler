for e in range(7):
	for i in range(10**e,int(10**(e + 1)/6) + 1):
		digits = sorted(map(int,str(i)))
		if digits != sorted(map(int,str(2 * i))):
			continue
		if digits != sorted(map(int,str(3 * i))):
			continue
		if digits != sorted(map(int,str(4 * i))):
			continue
		if digits != sorted(map(int,str(5 * i))):
			continue
		if digits != sorted(map(int,str(6 * i))):
			continue
		print(i)