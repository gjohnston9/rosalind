import numpy as np

with open("in.txt") as infile, open("out.txt", "w") as outfile:
	string = infile.readline().strip()
	infile.readline() # separating line
	alphabet = dict((char, index) for index, char in enumerate(infile.readline().strip().split()))
	infile.readline() # separating line
	path = infile.readline().strip()
	infile.readline() # separating line
	states = dict((state, index) for index, state in enumerate(infile.readline().strip().split()))
	infile.readline() # separating lines
	infile.readline() # separating lines
	print(string)
	print(path)
	print(states)
	t = np.zeros( (len(states), len(alphabet)));
	for row, line in enumerate(infile.readlines()):
		for col, prob in enumerate(line.split()[1:]):
			t[row][col] = prob
	print(t)
	prob = 1
	for path_char, emission_char in zip(path, string):
		prob *= t[states[path_char]][alphabet[emission_char]]
	print(prob)
	outfile.write(str(prob))