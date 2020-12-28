def runLengthEncoding(string):
    # if it is greater than 10, break it up
	recent = string[0]
	count = 1
	final = ''
	for i in range(1, len(string)):
		if string[i] == recent:
			# handle if count > 9
			
			if count == 9:
				final += (str(count) + recent)
				count = 1
			else:
				count += 1
		else:
			final += (str(count) + recent)
			recent = string[i]
			count = 1
	# add the final one
	final += (str(count) + recent)
	
	return final
		
		
