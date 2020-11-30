def smallestDifference(arrayOne, arrayTwo):
    ### pointers
	idx1 = 0
	idx2 = 0
	closest = []
	arrayOne.sort()
	arrayTwo.sort()
	current = float("inf")
	smallest = float("inf")
	while idx2 < len(arrayTwo) and idx1 < len(arrayOne):
		first = arrayOne[idx1]
		second = arrayTwo[idx2]
		if first < second:
			current = second - first
			idx1 += 1
		elif second < first:
			current = first - second
			idx2 += 1
		else:
			return [first, second]
		if smallest > current:
			smallest = current
			closest = [first, second]
	return closest
