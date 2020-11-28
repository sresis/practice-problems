def binarySearch(array, target):
	def bns_helper(array, target, left, right):
		if left > right:
			return -1
		
		mid =  (left + right) // 2
		
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			return bns_helper(array, target, left, mid - 1)
		else:
			return bns_helper(array, target, mid + 1, right)
	
	return bns_helper(array, target, 0, len(array)-1)
	