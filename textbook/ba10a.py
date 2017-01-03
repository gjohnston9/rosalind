import numpy as np

with open("in.txt") as infile, open("out.txt", "w") as outfile:
	path = infile.readline().strip()
	infile.readline() # separating line
	states = dict((state, index) for index, state in enumerate(infile.readline().strip().split()))
	infile.readline() # separating lines
	infile.readline() # separating lines
	t = np.zeros( (len(states), len(states)));
	for row, line in enumerate(infile.readlines()):
		for col, prob in enumerate(line.split()[1:]):
			t[row][col] = prob
	print(path)
	print(states)
	print(t)
	prob = 1 / float(len(states)) # probability of starting in initial state in path (initial probabilities are equal)
	cur = path[0]
	for char in path[1:]:
		prob *= t[states[cur]][states[char]]
		cur = char
	print(prob)
	outfile.write(str(prob))