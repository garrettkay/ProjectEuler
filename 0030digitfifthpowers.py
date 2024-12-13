sumoffifths = []
digitpowers = {
	1:1,
	2:32,
	3:243,
	4:1024,
	5:3125,
	6:7776,
	7:16807,
	8:32768,
	9:59049,
	0:0
}

for i in range(354295):
	n = i
	powersum = 0
	while n != 0:
		powersum += digitpowers[n % 10]
		if powersum > i:
			break
		n //= 10
	if powersum == i:
		sumoffifths.append(i)

print(sumoffifths)
print(sum(sumoffifths[2:]))