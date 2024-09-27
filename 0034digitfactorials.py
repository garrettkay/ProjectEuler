import time
from itertools import combinations_with_replacement as combr

start = time.time()

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
digitfactorials = []

for r in range(1,8):
	for comb in list(combr([1,2,3,4,5,6,7,8,9],r)):
		comb = list(comb)
		factsum = 0
		for digit in comb:
			factsum += fact[digit]
		if sorted(list(map(int,str(factsum)))) == comb:
			digitfactorials.append(factsum)
		for i in range(1,8-r):
			comb.insert(0,0)
			if sorted(list(map(int,str(factsum + i)))) == comb:
				digitfactorials.append(factsum + i)

print(digitfactorials)

end = time.time()
print(end-start)