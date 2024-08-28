import itertools

decimalpalindromes = set()
dbpalindromes = set()

for r in range(1,4):
	prods = set(itertools.product([1,2,3,4,5,6,7,8,9,0],repeat = r))
	for prod in prods:
		if prod[0] == 0:
			continue
		prodstring = "".join(map(str,prod))
		decimalpalindromes.update({int(prodstring + prodstring[::-1]),int(prodstring[:-1] + prodstring[::-1])})

for palindrome in decimalpalindromes:
	binary = bin(palindrome)[2:]
	if binary == binary[::-1]:
		dbpalindromes.add(palindrome)

print(sorted(dbpalindromes))
print(sum(dbpalindromes))