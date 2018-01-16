# e_sieve.py
from math import sqrt,floor

n = 169
# sn = math.floor(math.sqrt(n))
if n > 20:
    sn = floor(sqrt(n))
else:
    sn = n
print(n,sn)

sieve = {x:1 for x in range(2,n+1)}
sieve[2] = 1

for i in range(2,sn):
	# print(i)
	if sieve[i] == 1:
		print(sieve[i])
		for j in range(i**2,n+1,i):
			# print(j)
			sieve[j] = 0

print(sieve)
print([x for x in sieve if sieve[x] == 1])


print(sqrt(300),sqrt(350))