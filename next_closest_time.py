# next_closest_time.py

def next_closest_time(time):
	# convert time string to minutes 
	res = start = 60*int(time[:2]) + int(time[3:])
	maxtime = 60*24		# max number of minutes

	# parse into dict
	digits = {int(c) for c in time if c != ':'}

	# iterate through cartesian product of digits
	for h1 in digits:		#
		for h2 in digits:	#	hours
			for m1 in digits:		# 
				for m2 in digits:	# minutes
					# 
					hours, mins = 10*h1 + h2, 10*m1 + m2

					# reject values that can't be displayed on a clock
					if hours < 24 and mins < 60:
						testmins = hours*60 + mins
						modtestmins = (testmins-start)%(24*60)
						# reject values that exceed the maxtime
						if 0 < modtestmins < maxtime:
							res = testmins 	# update the result
							# reduce the maxtime to achieve "closest next" time
							maxtime = modtestmins

	# return time formated string
	return "%02d:%02d" % divmod(res,60)


# test = "19:34"
test = "23:59"
# test = "02:22"

print(next_closest_time(test))