import math

def abundant(n):
	factors = set([1])
	for i in range(2,int(math.sqrt(n)) + 1):
		if n % i == 0:
			factors.update({i,n//i})
	if sum(factors) > n:
		return True
	else:
		return False

abundantnums = set()

for n in range(1,28124):
	if abundant(n):
		abundantnums.add(n)

abundantsums = set()

for num1 in abundantnums:
	# Iterate through each element in the second set
	for num2 in abundantnums:
		# Compute the sum and add it to the result set
		abundantsums.add(num1 + num2)

print(abundantsums)

sum = 0
for i in range(1,28124):
	if i not in abundantsums:
		sum += i
print(sum)