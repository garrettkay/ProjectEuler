import numpy as np

primes = np.linspace(2,150001,150000)

for i in range(10001):
    if i >= np.size(primes):
        print("reached end, not enough starting values")
        break
    primes = np.delete(primes,((primes > primes[i]) & (primes % primes[i] == 0)))
    
print(primes)
print(int(primes[10000]))