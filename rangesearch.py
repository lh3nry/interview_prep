# rangesearch.py

def rangesearch(nums,target):
	lo, hi = 0, len(nums)-1

	# searching for left index
	while lo < hi:
		mi = (lo+hi)//2
		if nums[mi] >= target:
			hi = mi
		else:
			lo = mi+1
	left = lo

	# check if the target was found at all
	if nums[left] != target:
		return [-1,-1]
	hi = len(nums)-1

	# search for right index
	while lo < hi:
		mi = (lo+hi)//2
		if nums[mi] < target+1:
			lo = mi+1
		else:
			hi = mi


	if lo < 1:
		right = lo
	else:
		right = lo-1

	return [left,right]


testnums = [5,7,7,8,8,10]
testtarg = 8


print(rangesearch(testnums,testtarg))
print(rangesearch([1,2,3],2))
