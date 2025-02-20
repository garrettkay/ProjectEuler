import copy

def solveboard(b):
	board = copy.deepcopy(b)
	change = True
	while change:
		change = False
		for rc in range(81):
			r = rc // 9
			c = rc % 9
			if board[r][c] != 0:
				continue
			neighbors = {1,2,3,4,5,6,7,8,9}
			for i in range(9):
				neighbors.discard(board[r][i])
				neighbors.discard(board[i][c])
				neighbors.discard(board[r // 3 * 3 + i // 3][c // 3 * 3 + i % 3])
			if not neighbors:
				return (False,[])
			if len(neighbors) == 1:
				board[r][c] = neighbors.pop()
				change = True
	for rc in range(81):
		r = rc // 9
		c = rc % 9
		if board[r][c] == 0:
			neighbors = {1,2,3,4,5,6,7,8,9}
			for i in range(9):
				neighbors.discard(board[r][i])
				neighbors.discard(board[i][c])
				neighbors.discard(board[r // 3 * 3 + i // 3][c // 3 * 3 + i % 3])
			testboard = copy.deepcopy(board)
			for neighbor in neighbors:
				testboard[r][c] = neighbor
				simulatedboard = solveboard(testboard)
				if simulatedboard[0]:
					return simulatedboard
			return (False,[])
	return (True,board)

boards = []
with open("0096sudoku\\0096_sudoku.txt", 'r') as file:
	count = 0
	board = []
	for line in file:
		if count % 10 != 0:
			board.append(list(map(int,line.replace("\n",""))))
		if count % 10 == 9:
			boards.append(board)
			board = []
		count += 1

count = 0
for board in boards:
	count += int("".join(map(str,solveboard(board)[1][0][:3])))
print(count)