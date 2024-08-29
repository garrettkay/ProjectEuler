def nthdigit(n):
	exp = 0
	while True:
		if n <= (exp + 1) * 9 * 10 ** exp:
			return int(str(10 ** exp + (n - 1) // (exp + 1))[(n - 1) % (exp + 1)])
		n -= (exp + 1) * 9 * 10 ** exp
		exp += 1

prod = 1
for i in range(7):
	prod *= nthdigit(10 ** i)
print(prod)