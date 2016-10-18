# note: some of the structure for SuffixTreeNode is taken from here:
# http://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-6/

class SuffixTreeNode:
	def __init__(self, string, start, end, suffix_index=-1):
		"""
		(start, end) interval specifies the edge by which the node is connected to its parent
		node. Each edge will connect two nodes,  one parent and one child, and (start, end) interval
		 of a given edge  will be stored in the child node. Lets say there are two nodes A and B
		connected by an edge with indices (5, 8) then this indices (5, 8) will be stored in node B.

		for leaf nodes, the suffix_index stores the index of the suffix that starts at root and
		ends at this leaf
		"""
		self.start = start
		self.end = end

		self.children = set()
		self.string = string

		self.suffix_index = suffix_index


	def add_child(self, child):
		self.children.add(child)


	def get_next(self, next_string):
		"""
		returns either:
		a) None, meaning that this node contains the longest path from the
		root which matches a prefix of next_string, and the path ends exactly at this node; or
		b) a node, meaning that the longest path from the root that matches a prefix
		of next_string starts at the root but ends at the middle of the edge between the root and
		the returned node
		"""
		for child in self.children:
			if child.string[child.start : child.end].startswith(next_string):
				return child
		return None


	def __str__(self, level=0):
		ret = "\t"*level + "{}; {}~{}; {}\n".format(self.suffix_index, self.start, self.end,
			self.string[self.start:self.end])
		for child in self.children:
			ret += child.__str__(level+1)
		return ret


def suffix_tree_naive(string, end_char="$"):
	"""
	naive construction of suffix tree.
	Ukkonen's algorithm is next.
	"""
	string = string + end_char
	m = len(string)
	root = SuffixTreeNode(string, -1, -1, -1)
	root.add_child(SuffixTreeNode(string, 0, m, 0)) # add edge for suffix S[0:m]
	for i in range(1, m): # add suffix S[i:m] for 1 <= i < m
		nxt = root.get_next(string[i:m])
		if nxt == None:
			root.add_child(SuffixTreeNode(string, i, m, i))
		else:
			print "split the edge here~"
	return root


test = suffix_tree_naive("xab")
print test


monoisotopic_mass_table = {
	"A" : 71.03711,
	"C" : 103.00919,
	"D" : 115.02694,
	"E" : 129.04259,
	"F" : 147.06841,
	"G" : 57.02146,
	"H" : 137.05891,
	"I" : 113.08406,
	"K" : 128.09496,
	"L" : 113.08406,
	"M" : 131.04049,
	"N" : 114.04293,
	"P" : 97.05276,
	"Q" : 128.05858,
	"R" : 156.10111,
	"S" : 87.03203,
	"T" : 101.04768,
	"V" : 99.06841,
	"W" : 186.07931,
	"Y" : 163.06333 ,
}

RNA_codons = {
		"UUU" : "F",    "CUU" : "L",    "AUU" : "I",    "GUU" : "V",
		"UUC" : "F",    "CUC" : "L",    "AUC" : "I",    "GUC" : "V",
		"UUA" : "L",    "CUA" : "L",    "AUA" : "I",    "GUA" : "V",
		"UUG" : "L",    "CUG" : "L",    "AUG" : "M",    "GUG" : "V",
		"UCU" : "S",    "CCU" : "P",    "ACU" : "T",    "GCU" : "A",
		"UCC" : "S",    "CCC" : "P",    "ACC" : "T",    "GCC" : "A",
		"UCA" : "S",    "CCA" : "P",    "ACA" : "T",    "GCA" : "A",
		"UCG" : "S",    "CCG" : "P",    "ACG" : "T",    "GCG" : "A",
		"UAU" : "Y",    "CAU" : "H",    "AAU" : "N",    "GAU" : "D",
		"UAC" : "Y",    "CAC" : "H",    "AAC" : "N",    "GAC" : "D",
		"CAA" : "Q",    "AAA" : "K",    "GAA" : "E",    "GGA" : "G",
		"CAG" : "Q",    "AAG" : "K",    "GAG" : "E",    "AGA" : "R",
		"UGU" : "C",    "CGU" : "R",    "AGU" : "S",    "GGU" : "G",
		"UGC" : "C",    "CGC" : "R",    "AGC" : "S",    "GGC" : "G",
		"UGG" : "W",    "CGG" : "R",    "AGG" : "R",    "GGG" : "G",
		"CGA" : "R",
		"UAA" : "Stop", "UAG" : "Stop", "UGA" : "Stop",
	}

RNA_codons_rev = {
		"A" : ["GCU", "GCG", "GCC", "GCA"],
		"C" : ["UGC", "UGU"],
		"D" : ["GAU", "GAC"],
		"E" : ["GAA", "GAG"],
		"F" : ["UUU", "UUC"],
		"G" : ["GGU", "GGC", "GGG", "GGA"],
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
	"""
	not needed if using BioPython
	"""
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