# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier=1):
	output = 0
	for item in array:
		if type(item) is list:
			output += productSum(item, multiplier + 1)
		else:
			output += item
	return output * multiplier
				
				
				
		
		
