# sp_division.py
def divide(dividend,divisor):
	p,c = 0,divisor
	power = 1

	mul = divisor
	while (mul << 1) < dividend:
		# p = c
		mul <<= 1
		power<<=1

	# count2 = pow(2,power)
	ans = power
	print(p,c)
	residual = dividend - mul
	print(power,residual)
	while residual >= divisor:
		residual-=divisor
		ans+=1
	print(residual)
	return ans

	# result = 0
	# while dividend>=divisor:
	# 	s,power = divisor,1
	# 	while (s<<1) <= dividend:
	# 		s<<=1
	# 		power<<=1
	# 	result+=power
	# 	dividend-=s

	# return result

a = 21
b = 7

print(divide(a,b),a//b)