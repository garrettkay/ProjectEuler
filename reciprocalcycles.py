import math

valuemax = 0
cyclemax = 0

def reciprocalcycle(d):
	exponent = 1
	while True:
		if d == 1:
			return 0
		if d % 2 == 0:
			d //= 2
			continue
		if d % 5 == 0:
			d //= 5
			continue
		if (10 ** exponent - 1) % d == 0:
			return exponent
		exponent += 1

for i in range(1,1000):
	cycle = reciprocalcycle(i)
	if cycle > cyclemax:
		valuemax = i
		cyclemax = cycle

print(valuemax)
print(cyclemax)