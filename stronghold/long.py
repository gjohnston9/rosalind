# Genome Assembly as Shortest Superstring

from Bio import SeqIO


with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	DNA_strings = [str(fasta.seq) for fasta in fasta_sequences]
	ret = DNA_strings.pop()
	while len(DNA_strings) > 0:
		# print DNA_strings
		for string in DNA_strings:
			found = False
			for p in range(0, len(string) / 2 + 1):
				# check if this string can be attached to the beginning of ret
				if ret.startswith(string[p:]):
					ret = string[:p] + ret
					DNA_strings.remove(string)
					found = True
					break

			if not found:
				for p in range(len(string) / 2 - 1, len(string)):
					# check if this string can be attached to the end of ret
					if ret.endswith(string[:p]):
						ret = ret + string[p:]	
						DNA_strings.remove(string)
						found = True
						break

			if found:
				break

	outfile.write(ret)
