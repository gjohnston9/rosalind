# Perfect Matchings and RNA Secondary Structures

from Bio import SeqIO

from math import factorial

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	DNA = str(fasta_sequences.next().seq)
	G = DNA.count("G")
	A = DNA.count("A")

	outfile.write(str(factorial(G) * factorial(A)))
