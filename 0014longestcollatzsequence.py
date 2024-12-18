collatz = {1:1}

maxkey = 1
maxseq = 1

for n in range (2,1000000):
	seq = []
	i = n
	while True:
		try:
			index = collatz[i]
			if len(seq) + index > maxseq:
				maxseq = len(seq) + index
				maxkey = seq[0]
			for j in range(1,len(seq)+1):
				collatz[seq[-j]] = index + j
			break
		except:
			seq.append(i)

			if i % 2 == 0:
				i //= 2
			else:
				i = 3 * i + 1

print("Starting value of:",str(maxkey),"Gives sequence of length:",str(maxseq))