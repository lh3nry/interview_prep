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

print("test project build order")
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


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    G = dict()
    q = []	# queue
    v = []	# "visited" nodes

    # initialize the graph data structure
    for i in range(numCourses):
        G[i] = (set(),set())
        
    # populate edges
    for c,p in prerequisites:
        # print(c,p)
        G[c][0].add(p)
        G[p][1].add(c)
        
    # print(G)

    # insert all zero-dependency courses into the queue
    for course,edges in G.items():
    	# print(course,edges)
    	if edges[0] == set():
    		q.append(course)

    # print(q)

    while q:
    	# pop head of queue
    	c = q.pop(0)
    	# if it was in the queue, then it's safe to "visit"
    	v.append(c)
    	# check whether other courses depend on c
    	reqs = G[c][1]

    	for r in reqs:
    		temp = set()
    		temp.add(c)
    		# only the outgoing edges will be updated
    		G[r] = (G[r][0] - temp,G[r][1])
    		# check if r now has no pre-reqs
    		if G[r][0] == set():
    			q.append(r)

    # print(v)

    return len(v) == numCourses

print("test course prerequisites")
print(canFinish(3,[[2,1],[1,0]]))
print(canFinish(2,[[0,1],[1,0]]))



