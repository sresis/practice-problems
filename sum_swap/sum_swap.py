"""Given 2 arrays of integers, find a pair off values that you can swap to give 2 arrays the same sum.

   >>> sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3])
   [4, 6]
   >>> sum_swap([3, 3, 4, 1, 3], [2, 5, 5])
   [3, 2]
  


"""
def sum_swap(arr1, arr2):
    # sum each array
    # find the difference
    # for the larger side, see if diff -n is in the other list
    arr1_sum = 0
    for item in arr1:
        arr1_sum += item
    arr2_sum = 0
    for item in arr2:
        arr2_sum += item
    diff = arr1_sum - arr2_sum
    for item in arr1:
       target = int(-(diff - (item* 2))/2)
       if target in arr2:
           return [item, target]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")