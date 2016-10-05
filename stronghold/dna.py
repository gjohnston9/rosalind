# Counting DNA Nucleotides

with open("rosalind_dna.txt", "r") as infile, open("out.txt", "w") as outfile:
	DNA_string = infile.readline()
	out = " ".join(str(DNA_string.count(char)) for char in ("A", "C", "G", "T"))
	outfile.write(out)
