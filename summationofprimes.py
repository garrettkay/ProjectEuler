import numpy

primes = numpy.linspace(1,1999999,1000000)
primes[0] = 2

for i in range(1,1000000):
    if i >= numpy.size(primes):
        break
    if primes[i]**2 > 2000000:
        break
    primes = numpy.delete(primes,((primes > primes[i]) & (primes % primes[i] == 0)))

print(primes)
print(numpy.sum(primes))