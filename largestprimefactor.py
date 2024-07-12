import math

def largestprimefactor(n):
    for i in range(2,math.floor(math.sqrt(n))):
        if n % i == 0:
            return largestprimefactor(int(n/i))
    return n

print(largestprimefactor(600851475143))