maxdigitsum = 0
for a in range(1,100):
    for b in range(1,100):
        digitsum = sum(map(int,str(a ** b)))
        if maxdigitsum < digitsum:
            maxdigitsum = digitsum
print(maxdigitsum)