edges = set()

with open("0079passcodederivation\\0079_keylog.txt", 'r') as file:
	for line in file:
		edges.add((int(line[0]),int(line[1])))
		edges.add((int(line[1]),int(line[2])))

def deletel1edge():
	for edge in edges:
		for node in range(10):
			if (edge[0],node) in edges and (node,edge[1]) in edges:
				edges.remove(edge)
				return True
	return False

while deletel1edge():
	pass

def deletel2edge():
	for edge in edges:
		for node1 in range(10):
			for node2 in range(10):
				if (edge[0],node1) in edges and (node1,node2) in edges and (node2,edge[1]) in edges:
					edges.remove(edge)
					return True
	return False

while deletel2edge():
	pass

print(edges)