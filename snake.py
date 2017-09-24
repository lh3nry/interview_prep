# snake.py
# sprl_path = []
def spiral(matrix,x,y,n,d):
	sprl_path.append(matrix[x][y])
	if x < d - 1:
		spiral(matrix,x+1,y,n,d)
	if x == d - 1 and y < n - 1:
		spiral(matrix,x,y+1,n,d)
	if y == n - 1 and x > 0:
		spiral(matrix,x-1,y,n,d)


def snake(matrix):
	n = len(matrix)
	d = len(matrix[0])
	print('nxd:',n*d)
	if n < 0 or d < 0:
		return []
	# spiral(matrix,0,0,n,d)
	sprl_path = []
	x = y = 0 
	i = j = 0
	# len(sprl_path) < n*d and 
	while j < n and i < d:
		for x in range(i,d-i):
			# print(matrix[y][x])
			sprl_path.append(matrix[y][x])
		for y in range(j+1,n-j):
			# print(matrix[y][x])
			sprl_path.append(matrix[y][x])
		if len(sprl_path) > n*d - 1: break
		for x in range(d-i-2,-1+i,-1):
			# print(matrix[y][x])
			sprl_path.append(matrix[y][x])
		for y in range(n-j-2,j,-1):
			# print(matrix[y][x])
			sprl_path.append(matrix[y][x])
		# print(i,j)
		# print('loop 1:',list(range(i,d-i)))
		# print('loop 2:',list(range(j+1,n-j)))
		# print('loop 3:',list(range(d-i-2,i,-1)))
		# print('loop 4:',list(range(n-1-j,j,-1)))
		i+=1
		j+=1
	return sprl_path


board = [[1,2,3],[4,5,6],[7,8,9]]
board2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
test = [1,2,3,6,9,8,7,4,5]
board3 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]


# sprl = snake(board2)
# print(sprl)
# print(len(sprl))
print(snake(board))
print(snake(board2))
print(snake(board3))
