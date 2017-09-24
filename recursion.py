# recursion.py
def count_r(n):
	if n == 0:
		return [n]
	print(n)
	return count_r(n-1) + [n]

# lis = []
lis = count_r(5)

print(lis)
