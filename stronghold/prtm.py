# Calculating Protein Mass

from util import monoisotopic_mass_table as mass_table

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	protein = infile.readline().strip("\n")
	weight = sum(mass_table[char] for char in protein)
	outfile.write(str(round(weight, 3)))
