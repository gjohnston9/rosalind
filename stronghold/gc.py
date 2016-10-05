# Computing GC Content

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	id_to_DNA = {}
	id_string = infile.readline().strip(">")
	while id_string != "":
		DNA = "" # start building DNA
		line = infile.readline()
		while len(line) > 0 and line[0] != ">": # keep reading until encountering id line or EOF
			DNA += line.strip("\n")
			line = infile.readline()
		id_to_DNA[id_string] = DNA # add DNA to dictionary
		id_string = line.strip(">") # set next id

	id_to_GC = {}
	for key in id_to_DNA:
		DNA = id_to_DNA[key].strip("\n")
		GC = float(DNA.count("G") + DNA.count("C")) / len(DNA) * 100 # get GC content
		id_to_GC[key] = GC

	max_id = max(id_to_GC.iterkeys(), key=lambda key: id_to_GC[key])
	max_GC_content = max(id_to_GC.values())

	outfile.write(max_id)
	outfile.write(str(max_GC_content))
