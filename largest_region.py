# largest_region.py
import pprint

def explore(board,r,c,x,y):
    if (not 0 <= x < c) or (not 0 <= y < r): return 0
    if board[x][y] == 0: return 0
    # print(x,y,board[x][y])

    count = 1
    board[x][y] = 0
    for i in range(-1,2):
        for j in range(-1,2):
            count += explore(board,r,c,x+i,y+j)

    return count

def getLargestRegion(board):
    r = len(board)
    c = len(board[0])

    count = 0
    for x in range(r):
        for y in range(c):
            if board[x][y] == 1:
                count = max(count,explore(board,r,c,x,y)) 


    return count

pp = pprint.PrettyPrinter(width=14)

test = [
[1, 1, 0, 0],
[0, 1, 1, 0],
[0, 0, 1, 0],
[1, 0, 0, 0]
]  

pp.pprint(test)
# print(explore(test,4,4,0,0))
print(getLargestRegion(test))
pp.pprint(test)

