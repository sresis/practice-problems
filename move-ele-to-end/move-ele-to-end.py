def moveElementToEnd(array, toMove):
	i = 0
	j = len(array) -1
	# swap them if j != target and i = target
	while i < j:
		while i < j and array[j] == toMove:
			j -= 1
			print(array)
		if array[i] == toMove:
			array[i], array[j] = array[j], array[i]
		i += 1
	return array
				