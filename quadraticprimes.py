import math

primes = set()

quad = lambda a,b,n: n ** 2 + a * n + b

def isPrime(n):
	if n < 2:
		return False
	if n in primes:
		return True
	for i in range(2,int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	primes.add(n)
	return True

for i in range(1001):
	isPrime(i)

primes1000 = primes.copy()
amax = 0
bmax = 0
nmax = 0
for b in primes1000:
	for a in range(-999,1000):
		print("a is " + str(a))
		print("b is " + str(b))
		n = 0
		while True:
			if not isPrime(quad(a,b,n)):
				if n > nmax:
					amax = a
					bmax = b
					nmax = n
				print("n is " + str(n))
				break
			n += 1

print(amax)
print(bmax)
print(nmax)