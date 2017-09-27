# trapping_water.py
import functools
import queue

@functools.total_ordering
class Square(object):
	def __init__(self, height,i,j):
		self.height = height
		self.row = i
		self.col = j

	# def __eq__(self, other):
	def __lt__(self, other):
		return self.height < other.height

	def __str__(self):
		return 'height: ' + str(self.height) + ' at: (' + str(self.row) + ',' + str(self.col) + ')'



# def trapping_water()


test = [ [1,4,3,1,3,2],
		 [3,2,1,3,2,4],
		 [2,3,3,2,3,1]
		]
sol = 12

lonqu = queue.PriorityQueue()

for i,row in enumerate(test):
	for j,h in enumerate(row):
		lonqu.put(Square(h,i,j))

print([sq.__str__() for sq in lonqu.queue])
