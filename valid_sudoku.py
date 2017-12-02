# valid_sudoku.py
import pprint as pp
def checksquare(o,board):
	seen = {}
	a,b = 3*o[0], 3*o[1]
	sq = []
	for i in range(3):
		for j in range(3):
			x = board[a+i][b+j]
			# print((a+i,b+j),x)
			sq.append(x)
			# if x != '.' and x in seen:
			# 	return False
			# seen[x] = 1

	# for i in range(3):
	# 	# for j in range(3):
	# 		print(sq[i*3+0],sq[i*3+1],sq[i*3+2])

	for x in sq:
		if x != '.' and x in seen:
			return False
		seen[x] = 1
	# print("sq pass")
	# print(" ")

	return True


def validate(board):
	pp.pprint(board)
	for row in board:
		seen = {}
		for x in row:
			# print(x)
			if x != '.' and x in seen:
				return False
			seen[x] = 1
	print("rows passed")


	for col in range(9):
		seen = {}
		for i in range(9):
			x = board[i][col]
			if x != '.' and x in seen:
				return False
			seen[x] = 1
	print("cols passed")

	for r in range(3):
		for c in range(3):
			if not checksquare((r,c),board):
				return False
	print("squares passed")


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

board2 = [[".",".","4",".",".",".","6","3","."],
[".",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".","9","."],
[".",".",".","5","6",".",".",".","."],
["4",".","3",".",".",".",".",".","1"],
[".",".",".","7",".",".",".",".","."],
[".",".",".","5",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]]

board3 = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".","3",".","."],[".",".",".","1","8",".",".",".","."],[".",".",".","7",".",".",".",".","."],[".",".",".",".","1",".","9","7","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3","6",".","1",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","2","."]]

# print(checksquare((0,3),board))
print(validate(board3))



