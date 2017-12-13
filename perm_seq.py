# perm_seq.py

def get_perm(n,k):
	k-=1

	numl = list(range(1,n+1))
	# print(numl)

	fac = [1] * n
	fac[0] = 1
	for i in range(1,n):
		fac[i] = fac[i-1]*i
	# print(fac)

	ans = []

	# print(k//fac[n-1],k%fac[n-1])
	for i in range(n,1,-1):
		ind = k//fac[i-1]
		k %= fac[i-1]
		# print(ind,numl[ind],k)
		ans.append(numl[ind])
		del numl[ind]

	ans.extend(numl)

	return "".join([str(i) for i in ans])



print(get_perm(4,5))