dfc = {145:1,169:3,363601:3,1454:3,871:2,45361:2,872:2,45362:2,1:1,2:1,0:1,40585:1}
fact = {
	0:1,
	1:1,
	2:2,
	3:6,
	4:24,
	5:120,
	6:720,
	7:5040,
	8:40320,
	9:362880
}

def factorialchain(i):
	diglist = list(map(int,str(i)))
	sum = 0
	for dig in diglist:
		sum += fact[int(dig)]
	return sum

count = 0
for n in range (2,1000000):
	seq = []
	i = n
	while True:
		try:
			index = dfc[i]
			for j in range(1,len(seq)+1):
				dfc[seq[-j]] = index + j
				if index + j == 60:
					count += 1
			break
		except:
			seq.append(i)
			i = factorialchain(i)

print(count)