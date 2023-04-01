from itertools import permutations


def possible_permutations(some_list):
	for el in list(permutations(some_list)):
		yield list(el)
