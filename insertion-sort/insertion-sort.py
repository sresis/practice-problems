def swap(num1, num2, array):
	array[num1], array[num2] = array[num2], array[num1]
		
def insertionSort(array):
    
	for i in range(len(array)):
		j = i
		while j > 0 and array[j] < array[j - 1]:
			swap(j, j-1, array)
			j -= 1
	return array