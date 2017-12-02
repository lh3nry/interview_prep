# permute_array.py

def permute_w(nums,permuted,acc):
	# print(nums)
	if len(permuted) == len(nums):
		# if permuted not in acc: 
		acc.append(permuted)
		print(acc,id(acc))
		print(permuted,id(permuted))
		return
	else:
		for x in range(len(nums)):
			# print(x)
			if nums[x] in permuted: continue
			permuted.append(nums[x])
			# left = nums[:x] + nums[x+1:]
			# print(left)
			permute_w(nums,permuted,acc)
			# print(
			permuted.pop()
			# )

  



def permute(nums):
	# print(nums)
	a,tmp,copy = [],[], nums
	permute_w(copy,tmp,a)
	print("")
	return a


arr = [1,2,3]

# print(permute([]))

a = permute(arr)
print(a,id(a))

