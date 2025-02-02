import collections

partitions = collections.defaultdict(int)
partitions[0] = 1

genpentanums = []
index = 0
def nextgenpentanum():
	global genpentanums
	global index
	genpentanum = lambda n: (n * (3 * n - 1)) // 2
	index += 1
	genpentanums.append(genpentanum(index))
	genpentanums.append(genpentanum(-index))

nextgenpentanum()

for n in range(1,100000):
	if n > genpentanums[-1]:
		nextgenpentanum()
	sum = 0
	for i in range(len(genpentanums)):
		sum += (1 if i % 4 in (0, 1) else -1) * partitions[n-genpentanums[i]]
	partitions[n] = sum
	if sum % 1000000 == 0:
		print(n,sum)
		break