"""
want the highest set of indices (if there are duplicates)
    >>> get_indices_of_item_weights([4, 6, 10, 15, 16], 21)
    [3, 1]

"""
def get_indices_of_item_weights(arr, limit):
  # get target for each value in arr
  
  # make dict here
  num_dict = {}
  for i in range(len(arr)-1, -1, -1):
    if arr[i] in num_dict:
      num_dict[arr[i]].append(i)
    else:
      num_dict[arr[i]] = [i]
  
  for i in range(len(arr)-1, -1, -1):
    target = limit - arr[i]
    # see if there is a match (excluding current val)
    if target in num_dict:
      j = num_dict[target][0]
      if i != j:
        if i > j:
          return [i, j]
        else:
          return [j, i]
      

  return []
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
