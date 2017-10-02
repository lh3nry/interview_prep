# trapping_water.py
import functools
import queue
import pprint as p
from enum import Enum

def trap2d(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height) - 1
    units = 0
    left_max = right_max = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max: 
                left_max = height[left]
            else:
                units += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else: 
                units += right_max - height[right]
            right -= 1
            
    return units

class State(Enum):
	VISITED = 1
	VISITING = 2
	UNVISITED = 3

@functools.total_ordering
class Square(object):
	def __init__(self, height,i,j, v):
		self.height = height
		self.row = i
		self.col = j
		self.state = v
		# self.visited = False

	# def __eq__(self, other):
	def __lt__(self, other):
		return self.height < other.height

	def __str__(self):
		return 'height: ' + str(self.height) + ' at: (' + str(self.row) + ',' + str(self.col) + '), ' + str(self.state)

def printPQueue(pq):		# not in priority ordering
	p.pprint([str(sq) for sq in pq.queue])

def initQueue(map,pq):		# inserts border of map into queue
	rows = len(map)
	cols = len(map[0])
	# enqueue map border
	for i,h in enumerate(map[0]):
		# print(h)
		pq.put(Square(h,0,i,State.VISITING))
	for i,h in enumerate(map[rows-1]):
		pq.put(Square(h,0,i,State.VISITING))

	for i in range(1,rows-1):
		for j in [0,cols-1]:
			# print(i,j)
			pq.put(Square(map[i][j],i,j,State.VISITING))

def checkNeighbours(pq,sq,map):
	n, m = len(map), len(map[0])
	r, c = sq.row, sq.col
	# up
	if r > 0:
		pq.put(Square(map[r-1][c],r-1,c,State.VISITING))
	# down
	if r < n:
		pq.put(Square(map[r+1][c],r+1,c,State.VISITING))
	# left
	if c > 0:
		pq.put(Square(map[r][c-1],r,c-1,State.VISITING))
	# right
	if c < m:
		pq.put(Square(map[r][c+1],r,c+1,State.VISITING))
	sq.state = State.VISITED

def trapping_water(heightMap):
	q = queue.PriorityQueue()

	rows = len(heightMap)
	cols = len(heightMap[0])
	
	hmax = 0
	# enqueue map border
	initQueue(heightMap,q)

	# while q.queue:


	printPQueue(q)


print(trap2d([0,1,0,2,1,0,1,3,2,1,2,1]))



test = [ [1,4,3,1,3,2],
		 [3,2,1,3,2,4],
		 [2,3,3,2,3,1]
		]
sol = 4

trapping_water(test)

# print(list(enumerate(test[0]))+list(enumerate(test[2])))

# lonqu = queue.PriorityQueue()

# for i,row in enumerate(test):
# 	for j,h in enumerate(row):
# 		lonqu.put(Square(h,i,j))

# # p.pprint([str(sq) for sq in lonqu.queue])
# while lonqu.queue:
# 	print(str(lonqu.get()))