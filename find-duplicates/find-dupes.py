"""

"""

def find_duplicates(arr1, arr2):
  # determine which array is longer and turn it into a st=e
  
    if len(arr1) == len(arr2) == 1:
      if arr1 == arr2:
        return arr1
    if len(arr1) > len(arr2):
      lookup_array = arr2
      iterate_array = arr1
    else:
      lookup_array = arr1
      iterate_array = arr2

    new_list = []
    # starting values for bns
    low_val = 0
    high_val = len(lookup_array) -1
    # do bns for each value in iterate array
    for i in range(len(iterate_array)):
      match = binarySearch(lookup_array, iterate_array[i])
      if match != -1:
  
        new_list.append(lookup_array[match])
        # remove it so we don't have duplicate

    return new_list
   
    
def binarySearch(arr, num):
    begin = 0
    end = len(arr) -1

    while (begin <= end):
        mid = begin + (end - begin) // 2
        if arr[mid] < num:
            begin = mid + 1
        elif arr[mid] == num:
            return mid
        else:
            end = mid - 1

    return -1














