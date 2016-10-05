# Inferring mRNA from Protein

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	RNA_codons_rev = {
		"A" : ["GCU", "GCG", "GCC", "GCA"],
		"C" : ["UGC", "UGU"],
		"D" : ["GAU", "GAC"],
		"E" : ["GAA", "GAG"],
		"F" : ["UUU", "UUC"],
		"G" : ["GGU", "GGC", "GGG",	"GGA"],
		"H" : ["CAU", "CAC"],
		"I" : ["AUC", "AUU", "AUA"],
		"K" : ["AAG", "AAA"],
		"L" : ["CUC", "UUA", "CUU", "UUG", "CUA", "CUG"],
		"M" : ["AUG"],
		"N" : ["AAU", "AAC"],
		"P" : ["CCU", "CCA", "CCG", "CCC"],
		"Q" : ["CAA", "CAG"],
		"R" : ["CGU", "CGG", "AGG", "CGA", "CGC", "AGA"],
		"S" : ["AGU", "AGC", "UCU", "UCC", "UCA", "UCG"],
		"T" : ["ACC", "ACA", "ACG", "ACU"],
		"V" : ["GUU", "GUC", "GUA", "GUG"],
		"W" : ["UGG"],
		"Y" : ["UAU", "UAC"],
		"Stop" : ["UAA", "UAG", "UGA"],
	}

	protein = infile.readline().strip("\n")
	total = 1
	for char in protein:
		total *= len(RNA_codons_rev[char])
		if total >= 1000000:
			total = total % 1000000
	total *= 3 # three possible stop codons
	total = total % 1000000

	outfile.write(str(total))
