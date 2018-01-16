# stairs.py

def backtrack(n):
	if n < 0: return 0
	if n == 0: return 1

	return backtrack(n-1) + backtrack(n-2) + backtrack(n-3)


def dynamic(n,sols):
	if n < 0: return 0
	if n == 0: return 1

	if n not in sols:
		s = dynamic(n-1,sols) + dynamic(n-2,sols) + dynamic(n-3,sols)
		sols[n] = s
	return sols[n]

print(backtrack(3))
print(backtrack(7))
print(dynamic(7,{}))