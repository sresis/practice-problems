def classPhotos(redShirtHeights, blueShirtHeights):
	# get the back row
	if max(redShirtHeights) > max(blueShirtHeights):
		redBack = True
	else:
		redBack = False

	redShirtHeights.sort()
	blueShirtHeights.sort()
	def checkHeights(arr1, arr2):
		for i in range(len(arr1)):
			if arr2[i] <= arr1[i]:
				return False
			else:
				i += 1
		return True
	if redBack == True:
		return checkHeights(blueShirtHeights, redShirtHeights)
	else:
		return checkHeights(redShirtHeights, blueShirtHeights)

