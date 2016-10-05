# Transcribing DNA into RNA

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	dna = infile.readline()
	outfile.write(dna.replace("T", "U"))
