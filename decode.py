# decode.py
def decode_worker(split_str):
	part1 = split_str[0]
	part2 = split_str[1]
	a, b = int(part1), int(part2)
	print(a,b)
	if b > 26: return 0
	if a < 26: return 1
	if a < 10 and b < 10: return 1
	if b == 0:
		if a <= 26: return 1
		if a > 26 and a < 100: return 0
	if a > 26:
		# if b < 10 and b > 0: return 1
		take_one = (part1[:-1],part1[-1:])
		if take_one[1] == "":
			take_one[1] == "0"
		t1 = decode_worker(take_one)
		if a < 100: t2 = 0 
		else:
			take_two = (part1[:-2], part1[-2:])
			if take_two[1] == "":
				take_two[1] == "0"
			t2 = decode_worker(take_two)
			# print(take_one,take_two)

		print('t1',t1,'t2',t2)
		return t1 + t2

def decode_string_fire(msg):
	# return decode_worker((msg,"0"))
	n = len(msg)
	print(msg)
	if n == 0: return 0
	previousWays = 0
	possibleWays = 1
	for i in range(n):
		if not msg[i].isdigit(): return 0
		temp = 0
		piece = msg[i-1:i+1]
		if msg[i] != '0':
			temp = possibleWays
		if i>0 and int(piece) < 27 and msg[i-1] != '0':
			temp += previousWays
		previousWays = possibleWays
		possibleWays = temp
		print(msg[i],possibleWays,piece)
	return possibleWays

def decode_string(s):
    if not s or s == "0":
        return 0
    double, single = 0, 1
    for i in range(1, len(s)):
        p, c = s[i-1], s[i] # p for previous, c for current
        if c == "0": 						# must consider "pc" together
            if not (p == "1" or p == "2"):	# check for legal p digits
                return 0
            else:
                double, single = single, 0
        elif p == "0":					# "must" consider "c" alone
            double, single = 0, double
        else:
            if 11 <= int(p+c) <= 26:	# range where two digits is valid
                double, single = single, single + double
            else: # we can't consider "pc" together
                double, single = 0, single + double
    return single + double


print(decode_string("21234"))	
print(decode_string("521"))	
print(decode_string("29"))	
print(decode_string("113021"))	
print(decode_string("2202"))	