"""Perform basic string compression using the counts of repeated characters.
If compressed string isn't smaller, return original string

   >>> compress_string('abcd')
   'abcd'
   >>> compress_string('abcdee')
   'abcdee'
   >>> compress_string('aabcccccaaa')
   'a2b1c5a3'
"""
def compress_string(string):
    # go through the string
    # if next char is same as current char, keep increasing count
    # reset the count when you get to new letter. then append new string with letter and count
    #like a stack? for current letter
    new_str = ''
    count = 1
    for i in range(len(string)-1):
        current_letter = string[i]

        if current_letter == string[i + 1]:
            count += 1
        else:
            new_str += string[i]
            new_str += str(count)
            count = 1
    new_str += string[i]
    new_str += str(count)
    if len(new_str) < len(string):
        return new_str
    else:
        return string




    #if length of new string > length of original string, return original

   

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")