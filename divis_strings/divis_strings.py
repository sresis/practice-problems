"""Find the smallest string that can be concatenated to form both strings.

For example::

   >>> divis_count('rbrb', 'rbrb')
   2
   >>> divis_count('lrbblrbb', 'lrbb')
   4
   >>> divis_count('bcdbcdbcd', 'bcdbcd')
   -1
   >>> divis_count('bcdbcdbcdbcd', 'bcdbcd')
   3
   >>> divis_count('abcabd', 'abc')
   -1
   >>> divis_count('abcabc', 'abd')
   -1
   >>> divis_count('bbb', 'b')
   1
   
"""


def divis_count(str1, str2):
    """Return the length of smallest string divisible by both strings."""

    # determine if str1 is divisible by str2
    # get length of each
    # if str2 * len diff = str1, it is a match
    diff_carryover = len(str1) % len(str2)
    len_diff = int(len(str1) / len(str2))
    if diff_carryover!= 0:
        return -1
    if str(str2 * len_diff) != str1:
        return -1
    # find smallest string that can be concatenated to make both str1 and str2
    else:
        # iterate through
        for i in range(len(str1)-1):
            # calculate the number of times
            if i == 0:
                if str1[0] * len(str1) == str1:
                    return 1
            elif len(str1) % (i+ 1) == 0:
                if str1[:i+1] * int((len(str1) / (i+ 1))) == str1:
                    return i + 1

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")