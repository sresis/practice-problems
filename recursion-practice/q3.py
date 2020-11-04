"""
Write a recursive function that takes a list of numbers 
and returns the largest number in the list.
>>> return_largest([4, 6, 8, 1, 0, 13, 2])
13
>>> return_largest([4, -2, 0, 4, 3])
4
"""
def return_largest(lst, biggest=None):
    # if this number is bigger than the previous

    if biggest is None and len(lst) > 0:
        biggest = lst[0]
    if lst[0] > biggest:
        biggest = lst[0]
    if len(lst) == 1:
        return biggest
    return return_largest(lst[1:], biggest)
    



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")