import sympy

def consecutiveprimesum():
	maxprime = 0
	maxlen = 0
	for start in range(1000):
		sum = 0
		for i in range(1,1000):
			sum += sympy.prime(i + start)
			if sum >= 1000000:
				if i <= maxlen:
					print("finished, no sequences with greater than",str(maxlen),"terms are possible")
					print(maxprime)
					print(maxlen)
					return
				break
			if i > maxlen and sympy.isprime(sum):
				maxprime = sum
				maxlen = i
	

consecutiveprimesum()