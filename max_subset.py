# max_prod_sub.py
def max_prod_sub(nums):
	# OPT = [0 for i in range(len(nums)+1)]
	# OPT[0] = 1

	# for i in range(1,len(nums) + 1):
	# 	print(nums[i-1],OPT[i-1])
	# 	OPT[i] = max(nums[i-1],nums[i-1]*OPT[i-2])
	# 	print(OPT)

	# return OPT[-1]

	optmin = optmax = ret = 0
	for x in nums:
		if x < 0:
			optmin, optmax = optmax, optmin

		optmax = max(x,optmax*x)
		optmin = min(x,optmin*x)

		# print(optmin,optmax)

		ret = max(ret,optmax)

	return ret

def max_sum_sub(nums):
	if len(nums) < 2:
		return nums[0]
	# if nums[0] < 0:
	# 	localmax = optmax = nums[0]
	# else:
	# 	localmax = optmax = 0

	localmax = optmax = float('-inf')


	for x in nums:
		localmax = max(x,x+localmax)
		optmax = max(optmax,localmax)
		print(localmax,optmax)

	return int(optmax)

test = [2,3,-2,4]
testsum = [-2,1,-3,4,-1,2,1,-5,4]


# print(max_prod_sub(test))
print(max_sum_sub([1,2]))