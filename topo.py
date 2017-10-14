# topo.py
import collections
import functools


def topological(projects, deps):
	G = dict()
	V = []


	# build graph data structure
	for proj in projects:
		G[proj] = set()
	for (d,p) in deps:
		G[p].add(d)
	print()


	while len(V) < len(projects):
		cnt_deps = [len(x) == 0 for x in G.values()]
		print(cnt_deps)
		if not functools.reduce(lambda x,y: x or y, cnt_deps):
			return []
		for proj in projects:
			
			# if the project has no dependencies
			if proj in G and G[proj] == set():
				# build the project
				V.append(proj)
				G.pop(proj)
		# remove recently built projects
		for proj in G:					
			G[proj] -= set(V)

	# print(V,G)

	return V





projects = ['a',
			'b',
			'c',
			'd',
			'e',
			'f',
			'g' ]

deps = [ ('f','a'),
		 ('f','b'),
		 ('f','c'),
		 ('c','a'),
		 ('b','a'),
		 ('a','e'),
		 ('b','e'),
		 ('d','g')
		 ]


print(topological(projects,deps))

deps = [ ('f','a'),
		 ('f','b'),
		 ('f','c'),
		 ('c','a'),
		 ('b','a'),
		 ('a','e'),
		 ('b','e'),
		 ('d','g'),
		 ('e','f') # circular
		 ]

print(topological(projects,deps))


# s = stack()

# s = [1,2,3]
# print(s.pop())
# print(s)