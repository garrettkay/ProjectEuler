import math

pentnums = dict()

def simpentagonal(upperbound):
	for b in range(1,upperbound):
		pentb = int((3 * b - 1) * b / 2)
		for a in range(1,b):
			penta = int((3 * a - 1) * a / 2)
			if ispentagonal(penta + pentb) and ispentagonal(pentb - penta):
				print("found " + str(pentb - penta))
				print(penta)
				print(pentb)
				print(penta + pentb)
				return 0
			
def ispentagonal(n):
	return ((1 + math.sqrt(1 + 24 * n)) / 6).is_integer()

simpentagonal(5000)