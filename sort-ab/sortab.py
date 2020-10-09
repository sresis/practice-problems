"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    # start in list b and go through it
    # ffor each item in list b, see if it is greater than a each number in a. 
    # if it is not, add it
    # you can then start at the next index for the next number in b
    tracker = 0
    for num in b:
        i = tracker
        if len(a) == 0 or num > max(a):
            a.append(num)
        else:
            while num > a[i]:
                i += 1
            a.insert(i, num)
            tracker = i
    return a



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")
