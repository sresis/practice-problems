"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    # make list of all numbers in range
    # get the min distance for each number
    # get the max min distance
    distances = [cafes[0], num_holes - cafes[-1] -1]



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
