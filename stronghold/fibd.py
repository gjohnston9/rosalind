# Mortal Fibonacci Rabbits

from collections import defaultdict

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	line = infile.readline()
	n, m = map(int, line.split())
	f = defaultdict(lambda : 0) # map month to number of rabbits
	f[2] = 1
	f[1] = 1
	f[0] = 1

	for i in range(3, n+1):
		f[i] = f[i-1] + f[i-2] - f[i-(m+1)]

	outfile.write(str(f[n]))
