# rotated_binsearch.py
def findmin(nums):
	lo, hi = 0, len(nums)-1
	while lo < hi:
		mi = (lo+hi)//2
		if nums[mi] > nums[hi]:
			lo = mi + 1
		else:
			hi = mi
	return (lo,nums[lo])


def search(nums, target):
	lo, hi = 0, len(nums) 

	while lo < hi:
		mi = (lo+hi)//2

		if (nums[mi] < nums[0]) == (target < nums[0]):
			test = nums[mi]
		else:
			test = float("-inf") if target < nums[0] else float("inf")
		print(test)

		if test < target:
			lo = mi + 1
		elif test > target:
			hi = mi
		else:
			return mi

	return -1


testarr = [4,5,6,7,0,1,2,3]

print(search(testarr,9))
print(findmin(testarr))