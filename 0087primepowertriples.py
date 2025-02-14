import sympy
import numpy as np

primes = np.array(list(sympy.primerange(2,7072)))
squprimes = (primes ** 2)[(primes ** 2) <= 50000000]
cubprimes = (primes ** 3)[(primes ** 3) <= 50000000]
quaprimes = (primes ** 4)[(primes ** 4) <= 50000000]

primepowertriples = set()
for prime2 in squprimes:
	for prime3 in cubprimes:
		for prime4 in quaprimes:
			ppt = prime2 + prime3 + prime4
			if ppt < 50000000:
				primepowertriples.add(ppt)

print(len(primepowertriples))