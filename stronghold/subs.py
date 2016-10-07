# Finding a Motif in DNA

# return indices of all locations of t as a substring of s (1-indexed)

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	s = infile.readline().strip("\n")
	t = infile.readline().strip("\n")

	indices = (str(i+1) for i in range(len(s)) if s[i : i + len(t)] == t)
	outfile.write(" ".join(indices))
