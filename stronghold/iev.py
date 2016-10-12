# Calculating Expected Offspring

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	num_couples = infile.readline().strip("\n")
	num_couples = map(float, num_couples.split())
	# index | genotype of couple
	#   0	|       AA-AA
	#   1	|       AA-Aa
	#   2	|       AA-aa
	#   3	|       Aa-Aa
	#   4	|       Aa-aa
	#   5	|       aa-aa
	avg_dominant_phenotype_offspring = [
		2 * num_couples[0],
		2 * num_couples[1],
		2 * num_couples[2],
		2 * num_couples[3] * 0.75,
		2 * num_couples[4] * 0.5,
		2 * num_couples[5] * 0,
	]

	outfile.write(str(sum(avg_dominant_phenotype_offspring)))
