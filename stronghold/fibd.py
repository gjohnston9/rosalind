# Mortal Fibonacci Rabbits
# not finished***

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	line = infile.readline()
	n, m = map(int, line.split())
	rabbits = [1] * n
	for i in range(2, m-1):
		rabbits[i] = rabbits[i-1] + k * rabbits[i-2]
	outfile.write(str(rabbits[n-1]))
