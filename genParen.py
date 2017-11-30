# genParen.py

def genParen_w(st,cl,op,n,acc):
	# print(st,acc,cl,op)
	if cl == op == n:
		print(st)
		acc.append("".join(st))
		return
	if cl + 1 <= n and cl + 1 <= op:
		genParen_w(st+[')'],cl+1,op,n,acc)
	if op + 1 <= n:
		genParen_w(st+['('],cl,op+1,n,acc)

	# invalid leaf?
	return

def genParen(n):
	st,acc = ['('],[]
	cl, op = 0,1

	genParen_w(st,cl,op,n,acc)

	return acc


print(genParen(3))