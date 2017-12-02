# sp_division.py
def divide(dividend,divisor):
	if divisor == 0: return -1
	if dividend == 0: return 0

	sign = not ((divisor < 0) ^ (dividend < 0))
	dividend = abs(dividend)
	divisor = abs(divisor)

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
	return ans if sign else -ans

a = -21
b = 7

print(divide(a,b),a//b)