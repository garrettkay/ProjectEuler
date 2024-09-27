def islychrel(n):
	for i in range(50):
		n += int(str(n)[::-1])
		if n == int(str(n)[::-1]):
			return False
	return True

count = 0
for n in range(1,10000):
	if islychrel(n):
		count += 1
print(count)