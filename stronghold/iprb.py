# Mendel's First Law

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	line = infile.readline().strip("\n").split()
	k, m, n = line[0], line[1], line[2]
	k, m, n = map(float, (k, m, n))
	total = k + m + n
	outcomes = [
		k * (k-1),
		k * m,
		k * n,
		m * k,
		m * (m-1) * 0.75,
		m * n * 0.5,
		n * k,
		n * m * 0.5,
		n * (n-1) * 0
	]
	prob = sum(outcomes) / (total * (total - 1))

	outfile.write(str(prob))
