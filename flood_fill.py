# flood_fill.py
import pprint as p

def flood_fill_mech(image, x,y, selColor,newColor):
	m,n = len(image),len(image[0])

	# base cases
	if (not 0 <= x < m) or (not 0 <= y < n):
		# bounds check
		return
	if image[x][y] != selColor:
		# region check
		return

	# update color at image(x,y)
	image[x][y] = newColor

	# North
	flood_fill_mech(image ,x-1,y, selColor,newColor)
	# East
	flood_fill_mech(image ,x,y+1, selColor,newColor)
	# South
	flood_fill_mech(image ,x+1,y, selColor,newColor)
	# West
	flood_fill_mech(image ,x,y-1, selColor,newColor)


def flood_fill(image, x,y, newColor):
	# test color
	selColor = image[x][y]

	flood_fill_mech(image, x,y, selColor,newColor)

testimg = [[1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 0],
           [1, 0, 0, 1, 1, 0, 1, 1],
           [1, 2, 2, 2, 2, 0, 1, 0],
           [1, 1, 1, 2, 2, 0, 1, 0],
           [1, 1, 1, 2, 2, 2, 2, 0],
           [1, 1, 1, 1, 1, 2, 1, 1],
           [1, 1, 1, 1, 1, 2, 2, 1],
         ]


p.pprint(testimg)
flood_fill(testimg,4,4,3)
p.pprint(testimg)
