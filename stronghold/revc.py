# Complementing a Strand of DNA

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	replace = {
		"G" : "C",
		"C" : "G",
		"A" : "T",
		"T" : "A",
		"\n" : "\n",
	}

	dna = infile.readline()
	outfile.write("".join(replace[char] for char in dna[::-1]))
