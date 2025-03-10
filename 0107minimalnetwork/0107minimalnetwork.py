import numpy as np

network = np.loadtxt('0107minimalnetwork\\0107_network.txt',delimiter=',',dtype=str)
network[network == '-'] = '0'
network = network.astype(int)

networksum = sum(sum(network)) // 2

network[network == 0] = 1000

mstcost = 0
countedvertices = [0]
uncountedvertices = list(range(1,40))

while uncountedvertices:
	minx,miny,minvalue = -1,-1,1000
	for x in countedvertices:
		for y in uncountedvertices:
			if network[x,y] < minvalue:
				minx,miny,minvalue = x,y,network[x,y]
	mstcost += minvalue
	countedvertices.append(miny)
	uncountedvertices.remove(miny)

print(networksum - mstcost)