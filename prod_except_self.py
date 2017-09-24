# prod_except_self.py
def prod_x_self(nums):
	if len(nums) < 2:
		return nums

	l = r = 1

	ans_arr = [1 for i in range(len(nums))]
	i,j = 0, len(nums) - 1
	while i < len(nums) - 1:
		l *= nums[i]		# accumulate from left
		r *= nums[j]		# accumulate from right
		ans_arr[i+1] *= l 	# skip the current factor (left)
		ans_arr[j-1] *= r 	# skip current factor (right)
		i+=1; j-=1
		print(ans_arr)


	# # print(ans_arr)
	# for i in range(len(nums)):
	# 	for j in range(len(nums)):
	# 		if j != i:
	# 			ans_arr[j] *= nums[i]
	# 	print(ans_arr)

	return ans_arr


test = [1,2,3,4,5]
print(prod_x_self(test))


'''
1,2,3,4

s: 1,  1,  1,  1
1: 1,  1,  1,  1
2: 2,  1,  2,  2
3: 6,  3,  2,  6
4: 24, 12, 8,  6



DP: store some intermediate products



'''