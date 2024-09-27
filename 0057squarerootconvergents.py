num = 2
den = 1

count = 0
for i in range(1000):
	num,den = den + 2 * num,num
	if len(str(num-den)) > len(str(den)):
		count += 1
print(count)