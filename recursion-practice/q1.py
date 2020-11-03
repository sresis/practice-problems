"""
Write a recursive function that takes in a list and prints each element in that list.
    >>> print_recursively([4, 5, 6])
    4
    5
    6
"""
def print_recursively(lst):
    """prints each element recursively."""
    if len(lst) == 0:
        return 
    print(lst[0])
    print_recursively(lst[1:])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")