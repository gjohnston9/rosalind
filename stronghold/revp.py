# Locating Restriction Sites

from Bio import SeqIO, Seq

from collections import defaultdict, namedtuple
import pdb

def is_reverse_complement(string, start, end):
	fwd = string[start : end + 1]
	return Seq.reverse_complement(fwd) == fwd

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	fasta = fasta_sequences.next()
	seq = str(fasta.seq)
	print seq

	complement = {
		"A" : "T",
		"T" : "A",
		"G" : "C",
		"C" : "G"
	}

	matches = defaultdict(list)

	rev_pal = namedtuple("Reverse_Palindrome", ["position", "length"])

	### for each position in string, keep track of all potential ends of a reverse complement starting at this position 
	for i in range(len(seq)):
		for j in range(i + 1, len(seq), 2):
			if seq[j] == complement[seq[i]]:
				matches[i] = matches[i] + [j]

	answers = set()

	for start, ends in matches.iteritems():
		longest = max(filter(lambda end: is_reverse_complement(seq, start, end), ends) or [None])
		if longest != None:
			length = longest - start + 1
			if 4 <= length <= 12:
				answers.add(rev_pal(position=start+1, length=length))

	for index, t in enumerate(sorted(list(answers), key=lambda tup: tup.position)):
		outfile.write("{} {}".format(t.position, t.length))
		if index != len(answers) - 1:
			outfile.write("\n")
