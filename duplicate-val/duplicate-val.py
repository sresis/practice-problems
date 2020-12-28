def firstDuplicateValue(array):
	# handle length of 1
	if len(array) == 1:
		return -1
    left = 0
	right = 1
	dupes = []
	
	while left < len(array)-1:
		
		if array[left] == array[right]:
			dupes.append(right)
			left += 1
			right = left + 1
		elif right == len(array) - 1:
			left += 1
			right = left + 1
		else: 
			right += 1
	# handle no duplicates
	if dupes == []:
		return -1
	# otherwise get the min
	first = min(dupes)
	return array[first]
