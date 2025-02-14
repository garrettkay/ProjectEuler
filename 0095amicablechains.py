import sympy

divisors = dict()
chainlinks = set([1])

def findchain(num):
	n = num
	chain = []
	while True:
		if n in chainlinks:
			return []
		try:
			divs = divisors[n]
		except:
			divs = sympy.divisors(n)[:-1]
			divisors[n] = divs
		n = sum(divs)
		if n in chain:
			return chain[chain.index(n):]
		if n > 1000000:
			for link in chain:
				chainlinks.add(link)
			return []
		chain.append(n)

maxchainlength = 0
maxchain = []
for i in range(2,1000000):
	chain = findchain(i)
	if len(chain) > maxchainlength:
		maxchainlength = len(chain)
		maxchain = chain

print(maxchain,maxchainlength)
print(min(maxchain))