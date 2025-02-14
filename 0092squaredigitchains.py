endsat1 = set([1])
endsat89 = set([89,145,42,20,4,16,37,58])

def squaredigitchainiterate(n):
	def squaredigit(dig):
		squares = {
		0:0,
		1:1,
		2:4,
		3:9,
		4:16,
		5:25,
		6:36,
		7:49,
		8:64,
		9:81
		}
		return squares[int(dig)]
	return sum(list(map(squaredigit,str(n))))

for i in range(1,10000000):
	n = i
	nums = [i]
	while True:
		if n in endsat1:
			for num in nums:
				endsat1.add(num)
			break
		if n in endsat89:
			for num in nums:
				endsat89.add(num)
			break
		n = squaredigitchainiterate(n)
		nums.append(n)

print(len(endsat89))