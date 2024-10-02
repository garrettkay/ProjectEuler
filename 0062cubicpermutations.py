cubebase = 1
cubeupperbound = 1

def generatecubes():
	global cubebase
	global cubeupperbound
	cubeset = set()
	while True:
		cube = cubebase ** 3
		if cube < 10 ** cubeupperbound:
			cubeset.add(cube)
			cubebase += 1
		else:
			cubeupperbound += 1
			return cubeset
	
def findcubicpermutations():
	for i in range(20):
		cubeset = generatecubes()
		cubedigits = dict()
		for cube in cubeset:
			cubedigits.update({cube:sorted(map(int,str(cube)))})
		values = sorted(cubedigits.values())
		for i in range(len(values) - 4):
			if values[i] == values[i + 1] and values[i] == values[i + 2] and values[i] == values[i + 3] and values[i] == values[i + 4]:
				for key in cubedigits.keys():
					if cubedigits[key] == values[i]:
						print(key)
				return
			
findcubicpermutations()