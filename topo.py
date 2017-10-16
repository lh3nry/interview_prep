# topo.py
# import collections
import queue
import functools


def topological(projects, deps):
	# Gin, Gout =  dict(), dict()
	G = dict()
	V = []
	q = []
	# pq = queue.PriorityQueue()


	# build graph data structure
	for proj in projects:
		# Gin[proj] = set()
		# Gout[proj] = set()
		G[proj] = (set(),set())
	for (d,p) in deps:
		# Gin[p].add(d)
		# Gout[d].add(p)
		G[p][0].add(d)
		G[d][1].add(p)



	proj_ptr = 0
	for proj in projects:
		if G[proj][0] == set():
			q.append(proj)
	# print(q)


	while q:
		p = q.pop(0)
		# add project without dependency
		V.append(p)
		# update the dependencies in G
		p_inout = G[p]
		# print(p,p_inout)
		for dep in p_inout[1]:	# iterate through dependencies of p
			G[dep] = (G[dep][0] - set(p),G[dep][1])
			# if dep now has no dependencies, add to the queue
			if G[dep][0] == set():
				q.append(dep)

	if len(V) < len(projects):
		# we have exhausted the queue so there are no more
		# zero-dependency projects left. But we have not 
		# built all the projects, so there is a circular dependency
		return []

	# print(G)

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
