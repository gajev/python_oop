def reverse_text(some_string):
	current_index = len(some_string) - 1
	while current_index >= 0:
		yield some_string[current_index]
		current_index -= 1