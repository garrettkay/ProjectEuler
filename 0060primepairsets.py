import sympy
import time

primes = dict()
primelist = list(sympy.sieve.primerange(1,10**6))
for i in range(len(primelist)):
	primes.update({i+1:primelist[i]})

concat2primes = dict()
concat3primes = dict()
concat4primes = dict()
concat5primes = dict()

def isconcat2prime(p,q):
	if not sympy.isprime(int(str(p) + str(q))):
		return False
	if not sympy.isprime(int(str(q) + str(p))):
		return False
	return True

def findconcat2primes(upper):
	for a in range(1,upper):
		p1 = primes[a]
		concataprimes = set()
		for b in range(a + 1,upper):
			p2 = primes[b]
			if isconcat2prime(p1,p2):
				concataprimes.add(b)
		if len(concataprimes) > 0:
			concat2primes.update({a:concataprimes})

def findconcat3primes():
	for a in concat2primes.keys():
		concataprimes = sorted(concat2primes[a])
		numconcataprimes = len(concataprimes)
		for i in range(numconcataprimes):
				for j in range(i + 1,numconcataprimes):
					b = concataprimes[i]
					c = concataprimes[j]
					try:
						if c in concat2primes[b]:
							if a in concat3primes.keys():
								concat3primes[a].add((b,c))
							else:
								concat3primes.update({a:{(b,c)}})
					except:
						continue

def findconcat4primes():
	for a in concat3primes.keys():
		for (b,c) in concat3primes[a]:
			try:
				for d in concat2primes[c]:
					if d in concat2primes[a] and d in concat2primes[b]:
						if a in concat4primes.keys():
							concat4primes[a].add((b,c,d))
						else:
							concat4primes.update({a:{(b,c,d)}})
			except:
				continue

def findconcat5primes():
	for a in concat4primes.keys():
		for (b,c,d) in concat4primes[a]:
			try:
				for e in concat2primes[d]:
					if e in concat2primes[a] and e in concat2primes[b] and e in concat2primes[c]:
						if a in concat5primes.keys():
							concat5primes[a].add((b,c,d,e))
						else:
							concat5primes.update({a:{(b,c,d,e)}})
			except:
				continue

findconcat2primes(2000)
findconcat3primes()
findconcat4primes()
findconcat5primes()

for a in concat5primes.keys():
	for (b,c,d,e) in concat5primes[a]:
		print(a,b,c,d,e)
		print(primes[a],primes[b],primes[c],primes[d],primes[e])
		print(primes[a] + primes[b] + primes[c] + primes[d] + primes[e])