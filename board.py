# board.py
# paths = []
tmp_str = []

def search(board,x,y,m,n,paths):
	# print('x,y',x,y)
	tmp_str.append(board[x][y])
	# print(tmp_str)
	if x<m-1:
		# print('x',x)
		search(board,x+1,y,m,n,paths)
	if y<n-1:
		# print('y',y)
		search(board,x,y+1,m,n,paths)
	if x==m-1 and y==n-1: 
		print('exit cond') 
		print(tmp_str)
		paths.append("".join(tmp_str))
		# print(paths)
		tmp_str.pop(-1)
		return
	tmp_str.pop(-1)

def find_exit(board):
	m = len(board)
	n = len(board[0])
	if n < 1 or m < 1:
		return
	paths = []
	search(board,0,0,m,n,paths)

	return paths




board = [['A', 'X'],
		 ['D', 'E']]

board2 = [
  ['A', 'B', 'C', 'D'],
  ['E', 'F', 'G', 'H'],
  ['I', 'J', 'K', 'L']
]
test2 = ['ABCDHL', 'ABCGHL', 'ABCGKL', 'ABFGHL', 
'ABFGKL', 'ABFJKL', 'AEFGHL', 'AEFGKL', 'AEFJKL', 'AEIJKL']

board3 = [
  ['A', 'B', 'C', 'D'],
  ['E', 'F', 'G', 'H'],
  ['I', 'J', 'K', 'L'],
  ['M', 'N', 'O', 'P']
]
test3 = ['ABCDHLP', 'ABCGHLP', 'ABCGKLP', 'ABCGKOP', 
'ABFGHLP', 'ABFGKLP', 'ABFGKOP', 'ABFJKLP', 'ABFJKOP', 
'ABFJNOP', 'AEFGHLP', 'AEFGKLP', 'AEFGKOP', 'AEFJKLP', 
'AEFJKOP', 'AEFJNOP', 'AEIJKLP', 'AEIJKOP', 'AEIJNOP', 'AEIMNOP']

def search_sum(grid, x,y, m,n, maxsum):
    this = grid[x][y]
    print('x',x,'y',y,'curtile',this)
    maxsum[0] += this
    if x<m-1:
        down = grid[x+1][y]
    else:
        down = -1
    if y<n-1:
        right = grid[x][y+1]
    else:
        right = -1
        
    if x==m-1 and y==n-1:
        print('found exit')
        return
        # return maxsum
    print('down',down,'right',right)    

    if down > right:
        search_sum(grid, x+1,y, m,n, maxsum)
    else:
        search_sum(grid, x,y+1, m,n, maxsum)

def matrix_max_sum_dfs(grid):
    m = len(grid)
    n = len(grid[0])
    
    for row in grid:
        print(row)
    
    maxsum = [0]
    search_sum(grid, 0,0, m,n, maxsum)
    
    return maxsum[0]

grid1 = [
	[1,1,1],
	[1,1,1],
	[1,1,1]
]

grid2 = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

grid3 = [
	[1,2,3],
	[4,5,6]
]

grid4 = [
	[0,0],
	[0,0]
]

grid5 = [
	[1,2],
	[3,4]
]

msum = matrix_max_sum_dfs(grid2)
print(msum)

# print([a[1:] for a in board[:]])
# p = find_exit(board)
# p = find_exit(board)
# p = find_exit(board3)
# print(p)
# print(set(p) == set(test3))
# print(list(set(test3) - set(p)))
# print(p)
