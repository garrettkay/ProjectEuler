summations = dict()

def numofdivisionsgreaterthanx(n,x):
	if n == 0:
		return 1
	if n < x:
		return 0
	if n == x:
		summations[(n,x)] = 1
		return 1
	try:
		return summations[(n,x)]
	except:
		sum = 0
		for i in range(n,0,-1):
			sum += numofdivisionsgreaterthanx(n - i, i)
			summations[(n,i)] = sum
		return sum

for n in range(1,101):
	numdiv = numofdivisionsgreaterthanx(n,1)
print(summations[(100,1)] - 1)