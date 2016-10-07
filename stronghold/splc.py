# RNA Splicing

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	fasta = fasta_sequences.next()
	coding_DNA = str(fasta.seq)

	# remaining sequences are introns.
	# go through and remove them.
	for fasta in fasta_sequences:
		intron = str(fasta.seq)
		coding_DNA = coding_DNA.replace(intron, "")

	coding_DNA = Seq(coding_DNA, IUPAC.unambiguous_dna)
	mRNA = coding_DNA.transcribe()
	protein = mRNA.translate(stop_symbol="", to_stop=False)

	outfile.write(str(protein))
