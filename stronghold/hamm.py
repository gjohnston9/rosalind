# Counting Point Mutations

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	str1 = infile.readline().strip("\n")
	str2 = infile.readline().strip("\n")

	outfile.write(str(sum(1 for i in range(len(str1)) if str1[i] != str2[i])))
