# Catalan Numbers and RNA Secondary Structures

from Bio import SeqIO

def catalan(n):
	"""
	calculate the nth Catalan number
	(the Catalan numbers for n = 0, 1, 2, 3 are 1, 1, 2, 5 respectively)
	"""
	if n < 2:
		return 1
	arr = [1] * (n+1)
	for i in range(1, n+1):
		arr[i] = 0
		for j in range(0, i):
			arr[i] += arr[j] * arr[i-j-1]
	return arr[n]

def non_crossing_perfect_matchings(RNA, mod=1000000):
	"""
	given a string of RNA, calculate the number of possible
	non-crossing perfect matchings, mod 1000000 by default
	"""
	pairings = {
		"A" : "U",
		"U" : "A",
		"G" : "C",
		"C" : "G",
	}

	# TODO: use dynamic programming

	if len(RNA) == 0:
		return 1
	elif len(RNA) == 2:
		return 1 if RNA[1] == pairings[RNA[0]] else 0
	elif len(RNA) % 2 != 0:
		return 0
	else:
		first = RNA[0]
		match = pairings[first]
		# get indices of all possible endpoints for an arc starting at RNA[0]
		indices = [index for index, char in enumerate(RNA) if char == match]
		total = 0
		for index in indices:
			total += non_crossing_perfect_matchings(RNA[1:index]) * non_crossing_perfect_matchings(RNA[index+1:])
		return total % mod

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	RNA = str(fasta_sequences.next().seq)

	outfile.write(str(non_crossing_perfect_matchings(RNA)))
