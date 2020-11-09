"""Determine if valid subseq

For example::

   >>> find_pairs([0, -1, -2, 2, 1], 1)
   [[1, 0], [0, -1], [-1, -2], [2, 1]]
   >>> find_pairs([33, 1, 2], -1)
   [[1, 2]]

x - y = k
sort by y values
x = k + y
make a dictionary of all values in list
the value is the x value for that y value
then, for each 


"""
def find_pairs(arr, k):
    """Return all pairs with k difference.""" 
    num_dict = {}
    final_arr = []
    for num in arr:
        x = num + k
        num_dict[x] = num
    for num in num_dict:
        if num in arr:
            final_arr.append([num, num_dict[num]])

    return final_arr


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
