# perfect_squares.py

def numSquares2(n):
	if n < 1: return 1

	countsq = [0]

	while len(countsq) <= n:
		m = len(countsq)
		numsq = float('inf')
		i = 1
		while i**2 <= m:
			numsq = min(numsq,countsq[m-i**2] + 1)
			i+=1
			# print(i,numsq)
		countsq.append(numsq)
		print(list(enumerate(countsq)))

	return countsq[-1]

print(numSquares2(12))