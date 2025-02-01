summations = dict({})

for n in range(1,101):
	for x in range(1,101):
		summations[(n,1,x)] = max(n//2 - x + 1,0)

def numofdivisionsgreaterthanx(n,d,x):
	try:
		return summations[(n,d,x)]
	except:
		sum = 0
		for i in range(x,n//d + 1):
			sum += numofdivisionsgreaterthanx(n - i, d - 1, i)
		if sum == 0:
			for j in range(x,n + 1):
				summations[(n,d,j)] = 0
		else:
			summations[(n,d,x)] = sum
		return sum

for n in range(2,101):
	for d in range(1,n):
		numofdivisionsgreaterthanx(n,d,1)

count = 0
for i in range(1,100):
	count += summations[(100,i,1)]
print(count)