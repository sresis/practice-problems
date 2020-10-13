"""Given two strings, write a function to check if they are one edit (or zero edits) away.
    Valid edits are: insert, remove, or replace a character. 
   >>> is_one_away('pale', 'ple')
   True

   >>> is_one_away('pales', 'pale')
   True

   >>> is_one_away('pale', 'bale')
   True
   >>> is_one_away('pale', 'bake')
   False
   >>> is_one_away('alla', 'ale')
   False
   >>> is_one_away('plea', 'bake')
   False
   >>> is_one_away('pale', 'ale')
   True
   >>> is_one_away('pale', 'ela')
   False
   >>> is_one_away('ale', 'alla')
   False
   >>> is_one_away('ale', 'kale')
   True


"""


def is_one_away(str1, str2):

    # if they are the same length, we need to replace a letter
    # if str1 > str2, then we would need to add a letter to str2
    # if str2 > str1, add a letter to str1
    diff_count = 0
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff_count += 1
    
    diff_len = False
    if len(str1) > len(str2):
        diff_len = True
        for i in range(len(str2)):
            if str1[i] != str2[i]:
                # then continue on the normal way
                str2 = str2[:i] + str1[i] + str2[i:]
                diff_count += 1
    
    elif len(str2) > len(str1):
        diff_len = True
        for i in range(len(str1)):
            if str2[i] != str1[i]:
                # then continue on the normal way
                str1 = str1[:i] + str2[i] + str1[i:]
                diff_count += 1
                
    

    if diff_count > 1:
        return False
    elif str2 != str1 and diff_len == True and diff_count == 1:
        return False
    else:
        return True



   

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")
