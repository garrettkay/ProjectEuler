f = lambda x: 1 - x + x ** 2 - x ** 3 + x ** 4 - x ** 5 + x ** 6 - x ** 7 + x ** 8 - x ** 9 + x ** 10

def lagrangepolynomial(n,x):
	sum = 0
	for i in range(1,n + 1):
		prod = 1
		div = 1
		for j in range(1,n + 1):
			if i == j:
				prod *= f(i)
			else:
				prod *= (x - j)
				div *= (i - j)
		sum += prod / div
	return sum

diff = 0
for n in range(15):
	if f(n + 1) != lagrangepolynomial(n,n + 1):
		diff += lagrangepolynomial(n,n + 1)
print(diff)