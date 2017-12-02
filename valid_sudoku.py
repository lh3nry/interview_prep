# valid_sudoku.py
import pprint as pp
def checksquare(o,board):
	seen = {}
	a,b = o[0], o[1]
	for i in range(3):
		for j in range(3):
			x = board[a+i][b+j]
			# print((a+i,b+j),x)
			if x != '.' and x in seen:
				return False
			seen[x] = 1
	return True


def validate(board):
	# pp.pprint(board)
	for row in board:
		seen = {}
		for x in row:
			# print(x)
			if x != '.' and x in seen:
				return False
			seen[x] = 1

	for col in range(9):
		seen = {}
		for i in range(9):
			if x != '.' and x in seen:
				return False
			seen[x] = 1

	for r in range(3):
		for c in range(3):
			if not checksquare((r,c),board):
				return False
	return True




board = [
[".","8","7","6","5","4","3","2","1"],
["2",".",".",".",".",".",".",".","."],
["3",".",".",".",".",".",".",".","."],
["4",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".",".","."],
["6",".",".",".",".",".",".",".","."],
["7",".",".",".",".",".",".",".","."],
["8",".",".",".",".",".",".",".","."],
["9",".",".",".",".",".",".",".","."]
]
# print(checksquare((0,3),board))
print(validate(board))