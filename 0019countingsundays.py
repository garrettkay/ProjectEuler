monthdays = (31,28,31,30,31,30,31,31,30,31,30,31)
day = 1

count = 0
for i in range(1,1200):
	if i % 48 == 38:
		day = (day + 29) % 7
	else:
		day = (day + monthdays[i  % 12]) % 7
	if day == 0:
		count += 1
print(count)