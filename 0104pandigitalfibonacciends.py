import math

a = 1
b = 1
i = 2

while True:
	i += 1
	a,b = b,a + b
	if b < 10 ** 12:
		continue
	if set(str(b % (10 ** 12))[-9:]) == {'1','2','3','4','5','6','7','8','9'} and set(str(b // (10 ** (math.floor(math.log10(b)) - 10)))[:9]) == {'1','2','3','4','5','6','7','8','9'}:
		print(i)
		break