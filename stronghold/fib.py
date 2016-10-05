# Rabbits and Recurrence Relations

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	line = infile.readline()
	n, k = map(int, line.split())
	rabbits = [1] * n
	for i in range(2, n):
		rabbits[i] = rabbits[i-1] + k * rabbits[i-2]
	outfile.write(str(rabbits[n-1]))
