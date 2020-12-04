def isMonotonic(array):
    if len(array) <= 1:
		return True
	
	# find if it is increasing or decreasing
	left = 0
	right = 1
	while right < len(array)-1 and array[left] == array[right]:
		right += 1
		left += 1
	increasing = (array[right] > array[left])
	# handle if you reached the end
	if right == len(array) -1:
		return True
	#reset vals and  check that rest are strictly increasing/decreasing
	while right < len(array):
		print(increasing)
		if increasing:
			if array[right] < array[left]:
				return False
			else:
				right += 1
				left += 1
		if increasing == False:
			if array[right] > array[left]:
				return False
			else:
				right += 1
				left += 1
	return True
	
		
		
		
		
		
		
		