powers = set()

for a in range(2,101):
	for b in range(a,101):
		powers.add(a ** b)
		powers.add(b ** a)

print(len(powers))