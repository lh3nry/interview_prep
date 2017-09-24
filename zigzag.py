# zigzag.py
import functools as ft
def zigzag(s,numrows):
	parts = [[] for i in range(numrows)]

	look = nextlook = 0

	for c in s:
		parts[look].append(c)
		# print(parts)
		# update the progression depending on the line extents
		if look == 0:				# at the "top" of the zig
			nextlook = 1
		if look == numrows - 1:		# at the "bottom" of the zig
			nextlook = -1
		look += nextlook

	retval = ft.reduce(lambda x,y: x+y, ["".join(substr) for substr in parts])

	return retval

test = "PAYPALISHIRING"
'''
P   A   H   N
 A P L S I I G
  Y   I   R
'''



print(zigzag(test,4))