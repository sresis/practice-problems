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
   
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""
    # keep track of how many are open
    parens = 0
    for item in phrase:
        if item == '(':
            parens += 1
        elif item == ')':
            parens -= 1
    if parens != 0:
        return False
    else:
        return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")