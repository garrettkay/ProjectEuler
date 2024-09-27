import itertools

primes = {0:2, 1:3, 2:5, 3:7, 4:11, 5:13, 6:17}
perms = set(itertools.permutations(range(10)))

def issubdivisible(permstring):
	for i in range(7):
		if int(permstring[i+1:i+4]) % primes[i] != 0:
			return False
	return True

sum = 0
for perm in perms:
	permstring = "".join(map(str,perm))
	if issubdivisible(permstring):
		sum += int(permstring)
print(sum)