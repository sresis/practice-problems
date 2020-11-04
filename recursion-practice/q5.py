"""
Write a recursive function that takes in a string and reverses it. 
Return the reversed string.


>>> reverse_string('abcd')
'dcba'


"""
def reverse_string(str, i = 0, stored=''):
    stored = str[i] + stored
    
    if len(stored) == len(str):
        return stored
    return reverse_string(str, i+1, stored)

    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")
