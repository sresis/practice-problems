"""Determine if string has all unique characters. 
Do this without using additional data structures.

   >>> is_unique('abcdefg')
   True
   >>> is_unique('aaa')
   False
   >>> is_unique('hello')
   False
   >>> is_unique('ball')
   False


"""
def is_unique(str):
    for i in range(len(str)):
        if str[i] in str[:i]:
            return False
    return True

   

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")