import numpy as np

hands = np.loadtxt('pokerhands\\pokerhands.txt',dtype=str,delimiter=" ")

cardvalues = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

def isflush(hand):
	suit = hand[0][1]
	for i in range(1,5):
		if suit != hand[i][1]:
			return False
	return True

def isstraight(hand):
	lowend = hand[0]
	for i in range(1,5):
		if hand[i] != lowend + i:
			return False
	return True

def handeval(hand):
	flush = isflush(hand)
	cards = np.sort(np.vectorize(lambda s: cardvalues[s[0]])(hand))
	straight = isstraight(cards)
	if flush and straight:
		return (9,[cards[4]])
	if flush:
		return (6,[cards[4]])
	if straight:
		return (5,[cards[4]])
	values,counts = np.unique(cards, return_counts=True)
	values = list(values)
	counts = list(counts)
	if 4 in counts:
		return (8,[values[counts.index(4)]])
	if 3 in counts:
		if 2 in counts:
			return (7,[values[counts.index(3)]])
		tripsvalue = values[counts.index(3)]
		values.remove(tripsvalue)
		return (4,[tripsvalue,values[1],values[0]])
	pairs = counts.count(2)
	if pairs == 2:
		highcardvalue = values[counts.index(1)]
		values.remove(highcardvalue)
		return (3,[values[1],values[0],highcardvalue])
	if pairs == 1:
		pairvalue = values[counts.index(2)]
		values.remove(pairvalue)
		return (2,[pairvalue,values[2],values[1],values[0]])
	if pairs == 0:
		return (1,list(np.flip(cards)))

count = 0
for hand in hands:
	p1strength = handeval(hand[0:5])
	p2strength = handeval(hand[5:10])
	if p1strength[0] < p2strength[0]:
		continue
	elif p1strength[0] > p2strength[0]:
		count += 1
		continue
	else:
		for i in range(len(p1strength[1])):
			if p1strength[1][i] < p2strength[1][i]:
				break
			elif p1strength[1][i] > p2strength[1][i]:
				count += 1
				break
print(count)