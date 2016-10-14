# Open Reading Frames

from Bio import Seq
from Bio import SeqIO

def chunks(l, n):
	return [l[i:i + n] for i in xrange(0, len(l), n)]

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	fasta = fasta_sequences.next()
	seq = fasta.seq
	proteins = set([])

	for strand in (seq, seq.reverse_complement()):
		strand = str(strand)

		for frame in range(3):
			codons = chunks(strand[frame:], 3)
			starts = [index for index, codon in enumerate(codons) if codon == "ATG"]

			if starts == []:
				continue

			for start in starts:
				stops = [index for index, codon in enumerate(codons) if codon in ("TAA", "TAG", "TGA") and index > start]
				if stops == []:
					continue
				stop = min(stops)
				to_translate = Seq.Seq("".join(codons[start : stop+1]))
				translated = to_translate.translate(to_stop=True)
				proteins.add(translated)
				print "translated: {}".format(translated)

	for protein in proteins:
		outfile.write(str(protein) + "\n")
