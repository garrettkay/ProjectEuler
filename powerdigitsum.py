n = 2**1000
print(n)

digitsum = 0
while n != 0:
	digitsum += n % 10
	n //= 10
print(digitsum)