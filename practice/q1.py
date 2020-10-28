"""Given 2 strings, determine if 1 string is a permutation of the other?

For example::

   >>> is_permutation('cd', 'dc')
   True
   >>> is_permutation('aab', 'aba')
   True
   >>> is_permutation('zzyy', 'yyyz')
   False

  
"""


def is_permutation(str1, str2):

    str1 = list(str1)
    str1.sort()
    str2 = list(str2)
    str2.sort()
    if str2 == str1:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")