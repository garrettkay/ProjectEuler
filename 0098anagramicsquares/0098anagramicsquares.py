import numpy as np
import collections

def isanagramicsquare(word1,word2,square1,square2):
	length = len(word1)
	dict1 = dict()
	for i in range(length):
		if word1[i] in dict1 and dict1[word1[i]] != int(str(square1)[i]):
			return False
		else:
			dict1[word1[i]] = str(square1)[i]
	reverse_dict = {}
	for key, value in dict1.items():
		if value in reverse_dict:
			return False
		reverse_dict[value] = key
	for i in range(length):
		if dict1[word2[i]] != str(square2)[i]:
			return False
	return True

words = np.loadtxt('0098anagramicsquares\\0098_words.txt',delimiter=',',quotechar='"',dtype=str)
sortedletters = collections.defaultdict(set)
for word in words:
	letters = tuple(sorted(word))
	sortedletters[letters].add(str(word))

squares = (np.linspace(1,100000,100000) ** 2).astype(int).astype(str)
sorteddigits = collections.defaultdict(set)
for square in squares:
	digits = tuple(sorted(square))
	sorteddigits[digits].add(str(square))

anagramwords = collections.defaultdict(list)
for letters in sortedletters:
	sort = tuple(sortedletters[letters])
	if len(sort) > 1:
		anagramwords[len(sort[0])].append(sort)

anagramsquares = collections.defaultdict(list)
for digits in sorteddigits:
	sort = tuple(sorteddigits[digits])
	if len(sort) > 1:
		anagramsquares[len(sort[0])].append(sort)

maxsquare = 0
for n in range(10):
	for words in anagramwords[n]:
		for i in range(len(words)):
			word1 = words[i]
			for j in range(i):
				word2 = words[j]
				for squares in anagramsquares[n]:
					for k in range(len(squares)):
						square1 = squares[k]
						for l in range(k):
							square2 = squares[l]
							if isanagramicsquare(word1,word2,square1,square2) or isanagramicsquare(word1,word2,square2,square1):
								if max(int(square1),int(square2)) > maxsquare:
									maxsquare = max(int(square1),int(square2))
print(maxsquare)