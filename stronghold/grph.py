# Overlap Graphs

from util import get_id_to_DNA

with open("in.txt", "r") as infile, open("out.txt", "w") as outfile:
	id_to_DNA = get_id_to_DNA(infile)

	# for key in id_to_DNA:
	# 	# remap each id to tuple containing prefix and suffix of key
	# 	# not the most efficient...
	# 	DNA = id_to_DNA[key]
	# 	id_to_DNA[key] = (DNA[:3], DNA[-3:])

	prefixes = {} # map each prefix to the id's of the DNA strings which it prefixes
	suffixes = {} # same for suffixes

	for id_string in id_to_DNA:
		DNA = id_to_DNA[id_string]
		prefix = DNA[:3]
		suffix = DNA[-3:]
		prefixes[prefix] = prefixes.get(prefix, []) + [id_string]
		suffixes[suffix] = suffixes.get(suffix, []) + [id_string]

	for suffix in suffixes:
		for id_string1 in suffixes[suffix]:
			for id_string2 in prefixes.get(suffix, []):
				if id_string1 != id_string2:
					outfile.write("{} {}\n".format(id_string1, id_string2))
