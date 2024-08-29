import math

ptriple = dict()
value = 0
max = 0

for a in range(1,293):
	for b in range(a,500):
		c = math.sqrt(a ** 2 + b ** 2)
		if a + b + c > 1000:
			break
		if c == math.floor(c):
			try:
				ptriple[a + b + int(c)] += 1
				if ptriple[a + b + int(c)] > max:
					max = ptriple[a + b + int(c)]
					value = a + b + int(c)
			except:
				ptriple.update({a + b + int(c):1})

print(ptriple)
print(value)
print(max)