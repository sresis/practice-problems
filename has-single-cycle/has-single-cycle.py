def hasSingleCycle(array):
    visited = []
	i = 0
	while len(visited) < len(array):
		if i not in visited:
			visited.append(i)
			next_idx = (array[i] + i) % len(array)
			if next_idx >= 0:
				i = next_idx
			else:
				i = next_idx + len(array)
		else:
			return False
	# check if it loops back to 0 at end
	if i == 0:
		return True
	return False