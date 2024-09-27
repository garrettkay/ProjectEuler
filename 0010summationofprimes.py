import numpy as np

primes = np.linspace(1,1999999,1000000)
primes[0] = 2

for i in range(1,1000000):
    if i >= np.size(primes):
        break
    if primes[i]**2 > 2000000:
        break
    primes = np.delete(primes,((primes > primes[i]) & (primes % primes[i] == 0)))

print(primes)
print(np.sum(primes))