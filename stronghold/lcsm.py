# Finding a Shared Motif

from Bio import SeqIO

with open("in.txt", "r") as infile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	fasta = fasta_sequences.next()
	dna = str(fasta.seq)

	print "DNA: {}".format(dna)

	
