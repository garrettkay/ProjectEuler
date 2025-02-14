import numpy as np

numerals = np.loadtxt('0089romannumerals\\0089_roman.txt',delimiter=',',dtype=str)

romandict = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000
}
numeraldict = {
	0:0,
	1:1,
	2:2,
	3:3,
	4:2,
	5:1,
	6:2,
	7:3,
	8:4,
	9:2
}

def romantoint(numeral):
	sum = 0
	lastvalue = 0
	for char in reversed(numeral):
		value = romandict[char]
		if value < lastvalue:
			sum -= value
		else:
			sum += value
		lastvalue = value
	return sum

count = 0
for numeral in numerals:
	digitlist = [0,0] + list(map(int,str(romantoint(numeral))))
	count += len(numeral) - (int(sum(digitlist[:-3])) + numeraldict[digitlist[-3]] + numeraldict[digitlist[-2]] + numeraldict[digitlist[-1]])
print(count)