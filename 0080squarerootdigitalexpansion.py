import decimal
import math

decimal.getcontext().prec=110

def digsumofroot(n):
	return sum(map(int,str(decimal.Decimal(n).sqrt()*10**101)[:100]))

count = 0
for i in range(100):
	if math.isqrt(i) ** 2 != i:
		count += digsumofroot(i)
print(count)