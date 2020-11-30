def kadanesAlgorithm(array):
    max_num = array[0]
	curr_max = array[0]
	for i in range(1, len(array)):
		num = array[i]
		curr_max = max(num, curr_max + num)
		max_num = max(max_num, curr_max)
	return max_num