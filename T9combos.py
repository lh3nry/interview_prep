# T9combos.py

def charFromNumber(digit):
	if digit == 1:
		return ["*"]
	if digit == 0:
		return [" "]
	if 1 < digit < 7:
		start = 97
		offset = (digit-2)*3
		i = start + offset
		return [chr(i),chr(i+1),chr(i+2)]
	if digit == 7:
		return ["p","q","r","s"]
	if digit == 8:
		return ["t","u","v"]
	if digit == 9:
		return ["w","x","y","z"]

def letterCombinations(digits):
	ds = digits[::-1]
	# print(ds)
	ans = None
	for d in ds:
		if not ans:
			ans = charFromNumber(int(d))
		else:
			tmp = []
			for ch in charFromNumber(int(d)):
				# print(ch)
				for sub in ans:
					tmp.append(ch+sub)
					# print(tmp)
			ans = tmp
	return ans

# print(charFromNumber(2))
# print(charFromNumber(5))
# print(charFromNumber(1))
# print(charFromNumber(0))
# print(charFromNumber(7))
# print(charFromNumber(8))
# print(charFromNumber(9))


print(letterCombinations("23"))