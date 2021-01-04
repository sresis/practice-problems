def getPermutations(array):
    output = []
	helper(array, [], output)
	return output
	
		
def helper(array, currentPerm, perms):
	"""helper function"""
	## append the current perm if the array is now empty
	if not len(array) and len(currentPerm):
		perms.append(currentPerm)
	# otherwise, continue recursively
	else:
		for i in range(len(array)):
			newArray = array[:i] + array[i+1:]
			newPerm = currentPerm + [array[i]]
			helper(newArray, newPerm, perms)