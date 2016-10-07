# Completing a Tree

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	n = int(infile.readline().strip("\n"))
	ccs = {} # maps each vertex to the connected component that it belongs to
	cc_counter = 0 # keeps track of how many connected components have been encountered so far
	for line in infile.readlines():
		a, b = (line.split().strip("\n")[i] for i in (0, 1))
		if not ccs.get(a) or ccs.get(b):
			ccs[a] = cc_counter
			ccs[b] = cc_counter
			cc

