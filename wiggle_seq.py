# wiggle_seq.py
def sign(x): return (x>0)-(x<0)

def wiggleMaxLength(nums):
	n = len(nums)
	if n < 2:
		return n

	up = down = 1

	for i in range(1,n):
		if nums[i] > nums[i-1]:		# wiggle up
			up = down + 1
		elif nums[i] < nums[i-1]:
			down = up + 1

	return max(up,down)


	# up = [0 for _ in range(n)]
	# down = [0 for _ in range(n)]
	# up[0] = down[0] = 1

	# for i in range(1,n):
	# 	if nums[i] > nums[i-1]:		# wiggle up
	# 		up[i] = down[i-1] + 1	# extend prev down length
	# 		down[i] = down[i-1]
	# 	elif nums[i] < nums[i-1]:
	# 		down[i] = up[i-1] + 1
	# 		up[i] = up[i-1]
	# 	else:
	# 		down[i] = down[i-1]
	# 		up[i] = up[i-1]
	# return max(up[n-1],down[n-1])


test = [1,17,5,10,13,15,10,5,16,8]
print(wiggleMaxLength(test))