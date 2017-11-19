# rangesearch.py

def rangesearch(nums,target):
	lo, hi = 0, len(nums)-1

	while lo < hi:
		mi = (lo+hi)//2
		# print(mi,nums[mi])
			# if nums[mi] > target:
			# 	hi = mi-1
			# elif nums[mi] < target:
			# 	lo = mi+1
			# else:
			# 	found = mi
			# 	break
		if nums[mi] >= target:
			hi = mi-1
		else:
			lo = mi+1
	left = lo
	if nums[left] != target:
		return [-1,-1]
	hi = len(nums)-1
	while lo < hi:
		mi = (lo+hi)//2
		if nums[mi] < target+1:
			lo = mi+1
		else:
			hi = mi-1
	if nums[lo] == target:
		right = lo
	else:
		right = lo-1

	return [left,right]


testnums = [5,7,7,8,8,10]
testtarg = 7


print(rangesearch(testnums,testtarg))
print(rangesearch([1,2,3],2))
