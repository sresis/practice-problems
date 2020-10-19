"""Write a method to replace all spaces in a string with '%20'.
You may assume that you are given the "true" length of the string

   >>> urlify('Mr John Smith', 13)
   'Mr%20John%20Smith'
   >>> urlify('Hello 20', 8)
   'Hello%2020'


"""
# alternate approach
# def urlify(string, num):
#     #turn it into array
#     # if it is not the last one, add %20
#     word_arr = string.split(' ')
#     new_str = ''
#     for i in range(len(word_arr)-1):
#         new_str += word_arr[i]
#         new_str += '%20'
#     new_str += word_arr[-1]
#     return new_str
def urlify(string, num):
    # count spaces
    space_count = 0
    for item in string:
        if item == ' ':
            space_count += 1
    new_len = num - space_count + (3 * space_count)
    print(new_len)
    # go through string backwards
    char_count = num
    # if character is a space, increase char count by 2 and add the '%20'
   

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")