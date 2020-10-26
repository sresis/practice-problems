"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""
    # count outer and count innter
    # if the counts equal, return true
    # if dict is blank, return true
    par_dict = {}
    for item in phrase:
        if item == '(' or item == ')':
            if item in par_dict:
                par_dict[item] += 1
            else:
                par_dict[item] = 1
    if par_dict:
        if '(' not in par_dict or ')' not in par_dict:
            return False
        if par_dict['('] == par_dict[')']:
            return True
        else:
            return False

    else:
        return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
