# group_anagrams.py
import copy

def buildDict(s):
	d = dict()
	for c in s:
		if c in d:
			d[c]+=1
		else:
			d[c] = 1
	return d

def newEntry(s):
	return [buildDict(s),[s]]

def g_anagram(strs):
	print(strs)

	if not strs: return []
	if len(strs) < 2: return [strs]
	
	struct = []
	for s in strs:
		if not struct:		# initialize the empty data structure
			struct.append(newEntry(s))
			continue
		added = False
		sdict = buildDict(s)
		for entry in struct:
			d = entry[0]
			if sdict == d:
				entry[1].append(s)
				added = True
				break
		if not added:
			struct.append(newEntry(s))


	# print(struct)
	return [i[1] for i in struct]

test = ["eat","tea","tan","ate","nat","bat"]
# test = ["eat","tan","nat","bat"]

print(g_anagram(test))

# print(buildDict("eat") == buildDict("tea"))
# print(buildDict("eat") == buildDict("tan"))
# print(buildDict("tee") == buildDict("te"))
print(buildDict("tan") == buildDict("nat"))