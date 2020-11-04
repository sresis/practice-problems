"""
Write a recursive function that takes in a list and flattens it. For example:

in: [1, 2, 3]
out: [1, 2, 3]

in: [1, [1, 2], 2, [3]]
out: [1, 1, 2, 2, 3]
"""
def flatten_list(lst, result=None):
    ## if length of item is > 1, flatten it
    result = result or []
    for el in lst:
        if type(el) is list:
            flatten(el, result)
        else:
            result.append(el)
    return result






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")
