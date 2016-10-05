# Translating RNA into Protein

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	RNA_codons = {
		"UUU" : "F",	"CUU" : "L",	"AUU" : "I",	"GUU" : "V",

		"UUC" : "F",  	"CUC" : "L",  	"AUC" : "I",  	"GUC" : "V",

		"UUA" : "L",  	"CUA" : "L",  	"AUA" : "I",  	"GUA" : "V",

		"UUG" : "L",  	"CUG" : "L",  	"AUG" : "M",  	"GUG" : "V",

		"UCU" : "S",  	"CCU" : "P",  	"ACU" : "T",  	"GCU" : "A",

		"UCC" : "S",  	"CCC" : "P",  	"ACC" : "T",	"GCC" : "A",

		"UCA" : "S",  	"CCA" : "P",  	"ACA" : "T",  	"GCA" : "A",

		"UCG" : "S",  	"CCG" : "P",  	"ACG" : "T",  	"GCG" : "A",

		"UAU" : "Y",  	"CAU" : "H",  	"AAU" : "N",  	"GAU" : "D",

		"UAC" : "Y",  	"CAC" : "H",  	"AAC" : "N",  	"GAC" : "D",

		"CAA" : "Q",  	"AAA" : "K",  	"GAA" : "E",	"GGA" : "G",

		"CAG" : "Q",  	"AAG" : "K",  	"GAG" : "E",	"AGA" : "R",

		"UGU" : "C",  	"CGU" : "R",  	"AGU" : "S",  	"GGU" : "G",

		"UGC" : "C",  	"CGC" : "R",  	"AGC" : "S",  	"GGC" : "G",

		"UGG" : "W",  	"CGG" : "R",  	"AGG" : "R",  	"GGG" : "G",

		"CGA" : "R",

		"UAA" : "Stop", "UAG" : "Stop", "UGA" : "Stop",
	}

	RNA = infile.readline().strip("\n")
	protein = ""
	counter = 0

	while RNA[counter : counter + 3] != "AUG":
		counter += 3

	while RNA_codons[RNA[counter : counter + 3]] != "Stop":
		protein += RNA_codons[RNA[counter : counter + 3]]
		counter += 3

	outfile.write(protein)
