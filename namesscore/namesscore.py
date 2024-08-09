import numpy as np

lettervalues = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

names = np.array(np.loadtxt('namesscore\\names.txt',dtype=str,delimiter=',',quotechar='"'))
names.sort()
names = names.T

totalvalues = 0
index = 1
while names.size != 0:
	name, names = names[0], names[1:]
	lettersum = 0
	for letter in name:
		lettersum += lettervalues[letter]
	totalvalues += (index * lettersum)
	index += 1

print(totalvalues)