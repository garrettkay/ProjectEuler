import sympy

def consecutiveprimesum():
	maxprime = 0
	maxlen = 0
	for start in range(100000):
		sum = 0
		for i in range(1,100000):
			sum += sympy.prime(i + start)
			if sum >= 1000000:
				if i - 1 < maxlen:
					return
				break
			if sympy.isprime(sum) and i > maxlen:
				print(sum)
				print(i)
				maxprime = sum
				maxlen = i
	print(maxprime)
	print(maxlen)

consecutiveprimesum()