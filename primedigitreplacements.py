import itertools
import sympy

perms = itertools.product([0,1,2,3,4,5,6,7,8,9,"*"],repeat = 6)
for perm in perms:
	if not "*" in perm:
		continue
	digitstring = "".join(map(str,perm))
	count = 0
	for i in range(1,10):
		if not sympy.isprime(int(digitstring.translate({42:48+i}))):
			count += 1
		if count == 2:
			break
	if count < 2:
		print(digitstring + " is an 8-family")