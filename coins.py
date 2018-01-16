# coins.py
def coin_bag(n,coins):
	arr = [0]*(n+1)
	for c in coins:
		# print("c =",c)
		if c <= n: arr[c] += 1	# can we use coin c at all?

		for m in range(c,n+1):
			# Start at m = c to eliminate (>= 0) branch
			# print("\tm =",m)
			# print("\t\tlookback",m-c,arr[m-c])
			arr[m] = arr[m] + arr[m-c]

	print(arr)
	return arr[n]


print(coin_bag(4,[1,2,3]))
print(coin_bag(10,[2,5,3,6]))
