def sumsquared(n):
    return (0.5*n*(n+1))**2
def sumsquares(n):
    sum = 0
    for i in range(n+1):
        sum += i**2
    return sum

ssd = int(sumsquared(100))
sss = sumsquares(100)
print(str(ssd),"-",str(sss),"=",str(ssd - sss))