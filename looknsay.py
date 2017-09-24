# looknsay.py
'''
1   1
2   11
3   21
4   1211
5   111221
6   3112211
7   13212221



'''

def look_and_say2(sequence_number):
	if sequence_number <= 0:
		return None
	output = "1"
	i = 1
	while i < sequence_number:
		temp = ""
		count = 1
		for j in range(1,len(output)):
			if output[j] == output[j-1]:
				count = count + 1
			else:
				temp = temp + str(count)            
				temp = temp + output[j - 1]
				count = 1
				
		temp = temp + str(count)            
		temp = temp + output[len(output) - 1]
		output = temp
		i = i + 1
	return output

def look_and_say(sequence_number):
    if sequence_number < 1:
        return None
    
    say = "1"
    for i in range(1,sequence_number):
        temp = ""
        count = 1
        for j in range(1,len(say)):
            if say[j] == say[j-1]:
                count += 1          # count repeating numbers
            else:           # combo broken
                # first say how many times the prev number repeated
                temp += str(count)  
                # now add the previous digit we were counting
                temp += say[j-1]
                # reset counter for next digit series
                count = 1   # always at least one occurrence
                
        # append counts for the digit series found
            # note that for sequence_number = 2, the inner loop 
            # won't be entered, so this will also account for that
        temp += str(count)
        temp += say[-1]
        # feedback loop
        say = temp
    return say  # say it

def look_and_say(n):
	if n < 1: return None
	# seq = [1,11]
	say = "1"
	# j = 1
	for j in range(1,n):
		temp = ""
		count = 1
		for i in range(1,len(say)):
			if say[i-1] == say[i]:	# count repeating digits
				count += 1
			else:			# we found a different number
				temp += str(count) + say[i-1]
				count = 1	# reset counter 
		# write out if all the digits happened to be the same
		temp += str(count) + say[-1]
		# update the return value
		say = temp
	return say
		


# print(look_and_say(1))
# print(look_and_say(7))
for i in range(1,10):
	print(look_and_say(i))



