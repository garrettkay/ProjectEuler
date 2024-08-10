m = 1
n = 1
count = 2
while n < 10 ** 999:
	m,n = n,m + n
	count += 1
print(count)