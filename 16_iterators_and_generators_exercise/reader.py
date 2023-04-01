def read_next(*different_number):
	for element in different_number:
		for current_value in element:
			yield current_value
