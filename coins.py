# coins.py
def coin_bag(n,coins):
	arr = [0]*(n+1)
	for c in coins:
		print("c =",c)
		if c <= n: arr[c] += 1
		for m in range(1,n+1):
			print("\tm =",m)
			if m-c >= 0:
				print("\t\tlookback",m-c,arr[m-c])
				arr[m] = arr[m] + arr[m-c]

	print(arr)


coin_bag(4,[1,2,3])
coin_bag(10,[2,5,3,6])
