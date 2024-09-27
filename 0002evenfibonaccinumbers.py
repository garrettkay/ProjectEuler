n1 = 1
n2 = 1

while n1 < 4000000:
    temp = n2
    n2 = n1 + n2
    n1 = temp

sumfibonacci = n2 - 1
print(sumfibonacci/2)