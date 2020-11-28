def longestPeak(array):
    longest = 0
	i = 1
	while i < len(array) - 1:
		# if it is not a peak
		if array[i - 1]  >= array[i] or array[i + 1] >= array[i]:
			i += 1
			continue
		left = i - 2
		while left >= 0 and array[left] < array[left + 1]:
			left -= 1
		right = i + 2
		while right < len(array) and array[right] < array[right - 1]:
			right += 1
		curr = right - left - 1
		longest = max(longest, curr)
		i = right
	return longest
				
