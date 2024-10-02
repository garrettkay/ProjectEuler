import itertools
import math

trinums = set()
sqnums = set()
pennums = set()
hexnums = set()
hepnums = set()
octnums = set()

perms = itertools.product([1,2,3,4,5,6,7,8,9,0],repeat = 4)

for perm in perms:
	n = int("".join(map(str,perm)))
	if perm[0] == 0:
		continue
	if ((-1 + math.sqrt(1 + 8 * n)) / 2).is_integer():
		trinums.add(n)
	if (math.sqrt(n)).is_integer():
		sqnums.add(n)
	if ((1 + math.sqrt(1 + 24 * n)) / 6).is_integer(): 
		pennums.add(n)
	if ((1 + math.sqrt(1 + 8 * n)) / 4).is_integer():
		hexnums.add(n)
	if ((3 + math.sqrt(9 + 40 * n)) / 10).is_integer():
		hepnums.add(n)
	if ((2 + math.sqrt(4 + 12 * n)) / 6).is_integer():
		octnums.add(n)

def createchains(basenums,figsets):
	chains = [(basenums,figsets)]
	for i in range(5):
		tempchains = []
		for chain in chains:
			newchains = nextlinks(chain[0],chain[1])
			if newchains != False:
				tempchains.extend(newchains)
		chains = tempchains
	return chains

def nextlinks(basenums,figsets):
	links = []
	for i in range(len(figsets)):
		for num in figsets[i]:
			if str(basenums[-1])[2:4] == str(num)[0:2]:
				links.append((basenums + [num],figsets[:i] + figsets[i + 1:]))
	if len(links) == 0:
		return False
	return links

chains = []
for trinum in trinums:
	figsets = [sqnums,pennums,hexnums,hepnums,octnums]
	for chain in createchains([trinum],figsets):
		if str(chain[0][-1])[2:4] == str(trinum)[0:2]:
			chains.append(chain[0])

print(chains)
for chain in chains:
	print(sum(chain))