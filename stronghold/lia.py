# Independent Alleles

from scipy.special import binom

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	line = infile.readline().strip("\n")
	k, N = map(int, line.split())

	total = 2**k

	prob = sum(binom(total, i) * 0.25**i * 0.75**(total-i) for i in range(N, total+1))

	outfile.write(str(round(prob, 3)))