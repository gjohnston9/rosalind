# Catalan Numbers and RNA Secondary Structures

from Bio import SeqIO

def motzkin(n):
	"""
	M[n] = M[n-1] + sum(2 <= k <= n)(M[k-2] * M[n-k])

	n  motzkin(n)
	0  1
	1  1
	2  2
	3  4
	4  9
	5  21
	6  51
	7  127
	"""
	arr = [1] * (n+1)
	for i in range(2, n+1):
		arr[i] = arr[i-1] + sum(arr[k-2] * arr[i-k] for k in range(2, i+1))
	return arr[n]


def non_crossing_matchings(RNA, known):
	pairings = {
		"A" : "U",
		"U" : "A",
		"G" : "C",
		"C" : "G",
	}

	if RNA in known:
		return known[RNA]

	if len(RNA) < 2:
		return 1
	elif len(RNA) == 2:
		first = RNA[0]
		return 2 if RNA[1] == pairings[first] else 1
	else:
		first = RNA[0]
		pair = pairings[first]
		answer = non_crossing_matchings(RNA[1 : ], known) + \
			sum(non_crossing_matchings(RNA[1 : k], known) * non_crossing_matchings(RNA[k+1 : ], known) * (RNA[k] == pair) \
			for k in range(1, len(RNA)))
		known[RNA] = answer % 1000000
		return answer % 1000000


with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	fasta_sequences = SeqIO.parse(infile, "fasta")
	RNA = str(fasta_sequences.next().seq)

	outfile.write(str(non_crossing_matchings(RNA, {})))
