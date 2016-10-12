# Finding a Spliced Motif

# find one collection of indices of s in which the symbols of t appear as a subsequence of s.

from Bio import SeqIO

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	s = str(fasta_sequences.next().seq)
	t = str(fasta_sequences.next().seq)

	i = 0
	indices = []
	for index, char in enumerate(s):
		if char == t[i]:
			i += 1
			indices.append(index + 1)
			if len(indices) == len(t):
				break

	outfile.write(" ".join(map(str, indices)))
