from math import factorial as f

n = f(100)
print(n)

digitsum = 0
while n != 0:
	digitsum += n % 10
	n //= 10
print(digitsum)