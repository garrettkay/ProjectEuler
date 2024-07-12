import math

def triangular(n):
    return 0.5 * n * (n+1)

mult3 = math.floor(999/3)
mult5 = math.floor(999/5)
mult15 = math.floor(999/15)

print(triangular(mult3) * 3 + triangular(mult5) * 5 - triangular(mult15) * 15)