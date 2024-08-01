import random

collatz = dict.fromkeys([1],1)

maxkey = 1
maxseq = 1

for n in range (2,1000000):
	print(n)
	seq = []
	i = n
	while True:
		try:
			index = collatz[i]
			if len(seq) + index > maxseq:
				maxseq = len(seq) + index
				maxkey = seq[0]
			for j in range(1,len(seq)+1):
				collatz.update({seq[-j]:index + j})
			break
		except:
			seq.append(i)

			if i % 2 == 0:
				i //= 2
			else:
				i = 3 * i + 1

print(maxkey)
print(maxseq)