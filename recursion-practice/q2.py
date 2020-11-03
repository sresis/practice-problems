"""
Write a recursive function that prints the numbers 1 through 5.
>>> print_5_range()
1
2
3
4
5
"""
def print_5_range(n = 1):
    if n <= 5:
        print(n)
        print_5_range(n+1)





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")