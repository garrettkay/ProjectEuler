import collections

landingodds = {
    0: {0: 1},
    1: {1: 1},
    2: {2: 14/16, 10: 1/16, 0: 1/16},
    3: {3: 1},
    4: {4: 1},
    5: {5: 1},
    6: {6: 1},
    7: {7: 6/16, 0: 1/16, 10: 1/16, 11: 1/16, 24: 1/16, 39: 1/16, 5: 1/16, 15: 2/16, 12: 1/16, 4: 1/16},
    8: {8: 1},
    9: {9: 1},
    10: {10: 1},
    11: {11: 1},
    12: {12: 1},
    13: {13: 1},
    14: {14: 1},
    15: {15: 1},
    16: {16: 1},
    17: {17: 1},
    18: {18: 1},
    19: {19: 1},
    20: {20: 1},
    21: {21: 1},
    22: {22: 6/16, 0: 1/16, 10: 1/16, 11: 1/16, 24: 1/16, 39: 1/16, 5: 1/16, 25: 2/16, 28: 1/16, 19: 1/16},
    23: {23: 1},
    24: {24: 1},
    25: {25: 1},
    26: {26: 1},
    27: {27: 14/16, 10: 1/16, 0: 1/16},
    28: {28: 1},
    29: {29: 1},
    30: {10: 1},
    31: {31: 1},
    32: {32: 1},
    33: {33: 14/16, 10: 1/16, 0: 1/16},
    34: {34: 1},
    35: {35: 1},
    36: {36: 6/16, 0: 1/16, 10: 1/16, 11: 1/16, 24: 1/16, 39: 1/16, 5: 3/16, 12: 1/16, 33: 14/256, 10: 1/256, 0: 1/256},
    37: {37: 1},
    38: {38: 1},
    39: {39: 1}
}

def simulateroll(start):
	results = collections.defaultdict(int)
	for landing in landingodds[(start + 2) % 40]:
		results[landing] += landingodds[(start + 2) % 40][landing] * 1 / 16
	for landing in landingodds[(start + 3) % 40]:
		results[landing] += landingodds[(start + 3) % 40][landing] * 2 / 16
	for landing in landingodds[(start + 4) % 40]:
		results[landing] += landingodds[(start + 4) % 40][landing] * 3 / 16
	for landing in landingodds[(start + 5) % 40]:
		results[landing] += landingodds[(start + 5) % 40][landing] * 4 / 16
	for landing in landingodds[(start + 6) % 40]:
		results[landing] += landingodds[(start + 6) % 40][landing] * 3 / 16
	for landing in landingodds[(start + 7) % 40]:
		results[landing] += landingodds[(start + 7) % 40][landing] * 2 / 16
	for landing in landingodds[(start + 8) % 40]:
		results[landing] += landingodds[(start + 8) % 40][landing] * 1 / 16
	return results

spotprobabilities = collections.defaultdict(lambda: 0.025)
for times in range(10):
	nextspotprobabilities = collections.defaultdict(int)
	for start in range(40):
		spotsim = simulateroll(start)
		for space in spotsim:
			nextspotprobabilities[space] += spotprobabilities[start] * spotsim[space]
	spotprobabilities = nextspotprobabilities

print(sorted(spotprobabilities, key=spotprobabilities.get, reverse=True)[:3])