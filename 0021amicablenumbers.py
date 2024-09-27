import math

factors = {1:{1}}
factors.update({2:{1:2}})

def factorize(n):
	factors = set([1])
	for i in range(2,int(math.sqrt(n)) + 1):
		if n % i == 0:
			factors.update({i,n//i})
	return factors

for i in range(3,10000):
	print(i)
	factors.update({i:factorize(i)})

sumammicable = 0
for i in range(2,10000):
	try:
		if i != sum(factors[i]) and i == sum(factors[sum(factors[i])]):
			sumammicable += (i + sum(factors[i]))
	except:
		continue
	try:
		factors.pop(sum(factors[i]))
		factors.pop(i)
	except:
		continue
print(sumammicable)