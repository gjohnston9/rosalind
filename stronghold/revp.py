# Locating Restriction Sites

from Bio import SeqIO, Seq

def palindromes(string, start, indices):


with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	fasta = fasta_sequences.next()
	fwd = str(fasta.seq)
	rev = Seq.reverse_complement(fwd)
	print fwd
	# print rev
	ind = {nuc : [index for index, char in enumerate(fwd) if char == nuc] for nuc in ("A", "T", "G", "C")}
	palindromes = set()
	print ind

