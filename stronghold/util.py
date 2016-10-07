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

def get_id_to_DNA(file):
	id_to_DNA = {}
	id_string = file.readline().strip(">\n")
	while id_string != "":
		DNA = "" # start building DNA
		line = file.readline()
		while len(line) > 0 and line[0] != ">": # keep reading until encountering id line or EOF
			DNA += line.strip("\n")
			line = file.readline()
		id_to_DNA[id_string] = DNA # add DNA to dictionary
		id_string = line.strip(">\n") # set next id
	return id_to_DNA