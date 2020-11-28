def threeNumberSum(array, targetSum):
	output = []
	# sort array
	array.sort()
	for i in range(len(array)):
		left = i + 1
		right = len(array) -1
		while left < right:
			if array[i] + array[left] + array[right] == targetSum:
				output.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif array[i] + array[left] + array[right] < targetSum:
				left += 1
			else:
				right -= 1
	return output
