partitions = dict()

def numofpartitionsgreaterthanx(n,x):
	if n == 0:
		return 1
	if n < x:
		return 0
	if n == x:
		partitions[(n,x)] = 1
		return 1
	try:
		return partitions[(n,x)]
	except:
		sum = 0
		for i in range(n,0,-1):
			sum += numofpartitionsgreaterthanx(n - i, i)
			partitions[(n,i)] = sum
		return sum

for n in range(1,101):
	numofpartitionsgreaterthanx(n,1)
print(partitions[(100,1)] - 1)