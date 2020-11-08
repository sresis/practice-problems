"""
1.
Input: 'abba', 'aba'
Output: False

2.
Input: 'breed', 'deerb'
Output: True

3. 
Input: 'abcd', 'abcb'
Output: False

Make a dictionary of each string
show the letter count for each letter
If the dictionaries are the same, return true

Otherwise, return false

"""

    


def is_permutation(str1, str2):
    """ Return true if they are permutations"""

    str1_dict = {}
    str2_dict = {}

    for char in str1:
        if char in str1_dict:
            str1_dict[char] += 1
        else:
            str1_dict[char] = 1

    for char in str2:
        if char in str2_dict:
            str2_dict[char] += 1
        else:
            str2_dict[char] = 1

    print(str1_dict)
    print(str2_dict)

    return str1_dict == str2_dict


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
