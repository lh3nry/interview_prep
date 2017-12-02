# sp_division.py
def divide(dividend,divisor):
	power = 1
	mul = divisor

	while (mul << 1) < dividend:
		mul <<= 1
		power<<=1

	ans = power

	residual = dividend - mul
	# print(power,residual)
	while residual >= divisor:
		residual-=divisor
		ans+=1
	# print(residual)
	return ans

a = 21
b = 7

print(divide(a,b),a//b)