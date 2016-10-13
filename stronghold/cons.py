# Consensus and Profile

from Bio import SeqIO

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	seqs = [str(sequence.seq) for sequence in fasta_sequences]
	# print seqs
	profile = {base : [0 for _ in range(len(seqs[0]))] for base in ("A", "C", "G", "T")}
	for sequence in seqs:
		for index, char in enumerate(sequence):
			profile[char][index] += 1
	# for key in profile:
	# 	print "{}: {}".format(key, profile[key])
	
	consensus = ""
	for i in range(len(seqs[0])):
		consensus += max(profile, key=lambda x: profile[x][i])

	outfile.write(consensus + "\n")

	for base in ("A", "C", "G", "T"):
		outfile.write("{}: {}\n".format(base, " ".join([str(i) for i in profile[base]])))