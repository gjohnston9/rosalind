# Enumerating Gene Orders

def permute(n):
	if n == 1:
		return [[1]]
	ret = []
	# print "n is: {}".format(n)
	for perm in permute(n-1):
		for i in range(len(perm)+1):
			ret.append(perm[:i] + [n] + perm[i:])
	return ret


with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	n = int(infile.readline())
	perms = permute(n)
	outfile.write("{}\n".format(len(perms)))
	outfile.write("\n".join(" ".join(str(num) for num in perm) for perm in perms))
