"""
Write a recursive function that takes a list of numbers 
and returns a list where all numbers are doubled.
>>> double_list([4, 2, 7])
[8, 4, 14]


"""
def double_list(lst, i=0):
    lst[i] = 2 * lst[i]
    if i == len(lst)-1:
        return lst
    return double_list(lst, i+1)
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")
