# Finding a Protein Motif

import collections
import urllib2
import re

motif = re.compile("(?=N(?!P)[A-Z][ST](?!P)[A-Z])")

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	answers = collections.OrderedDict()

	for line in infile.readlines():
		access_id = line.strip("\n")
		answers[access_id] = []

		fasta = urllib2.urlopen("http://www.uniprot.org/uniprot/{}.fasta".format(access_id))
		fasta.next() # ignore first line
		seq = "".join(line.strip("\n") for line in fasta)

		for m in motif.finditer(seq):
			answers[access_id] = answers[access_id] + [m.start() + 1]

	for answer in filter(lambda x: answers[x] != [], answers.keys()):
		outfile.write(answer + "\n")
		outfile.write(" ".join(str(a) for a in answers[answer]) + "\n")
