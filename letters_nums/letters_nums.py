"""Given an array filled with letters and numbers, find the longest subarray with equal number of letters and numbers.
    >>> longest_equal(['aabb1234', 'aabb12325', 'aa22332', 'a2b2'])
    'aabb1234'
    >>> longest_equal(['a2b2', 'aabb12345', '123ab1', 'a2'])
    'a2b2'

"""
def longest_equal(arr):
    # determine if number and letter count is the same
    # if it is, add to list
    equals = []
    for item in arr:
        al_count = 0
        num_count = 0
        for char in item:
            if char.isalpha():
                al_count += 1
            else:
                num_count += 1
        if al_count == num_count:
            equals.append(item)
    return max(equals)

         

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")
