# permute_array.py

def permute_w(nums,permuted,acc):
	# print(nums)
	if len(permuted) == len(nums):
		# if permuted not in acc: 
		new = list(permuted)
		acc.append(new)
		# print(acc,id(acc))
		# print(permuted,id(permuted))
		return
	else:
		for x in range(len(nums)):
			# print(x)
			if nums[x] in permuted: continue
			permuted.append(nums[x])
			permute_w(nums,permuted,acc)
			permuted.pop()



def permute(nums):
	a,tmp,copy = [],[], nums
	permute_w(copy,tmp,a)
	return a



def backtrack(pos,num,acc):
	if pos == len(num):
		# print(num)
		# construct new lists (gives new id so the recursion will work)
		new = list(num)
		# print(id(new),id(num))
		acc.append(new)
	else:
		for i in range(pos,len(num)):
			num[i],num[pos] = num[pos],num[i]
			backtrack(pos+1,num,acc)
			num[i],num[pos] = num[pos],num[i]



arr = [1,2,3,4]

# print(permute([]))

a = permute(arr)
print(a,id(a))
print("")

a = []
backtrack(0,arr,a)
print(a)

