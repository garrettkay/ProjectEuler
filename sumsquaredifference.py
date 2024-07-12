def sumsquared(n):
    return (0.5*n*(n+1))**2
def sumsquares(n):
    sum = 0
    for i in range(n+1):
        sum += i**2
    return sum

print(sumsquared(100))
print(sumsquares(100))
print(sumsquared(100) - sumsquares(100))