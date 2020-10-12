"""
Remove array elements that are in a given index range.

   >>> remove_array_elements([-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76], [[5, 8], [10, 13], [3, 6], [20, 25]])
   [-8, 3, -5, 29, 43, 76, 73, 76]


"""

def remove_array_elements(arr, ranges):
    # see if each element is any of the banned ranges
    final_range = []
    for i in range(len(arr)):
        incorrect_count = 0

        for item in ranges:
            if i >= item[0] and i < item[1]:
                incorrect_count += 1
        if incorrect_count == 0:
            final_range.append(arr[i])
    return final_range



    return [0,1]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.!\n")