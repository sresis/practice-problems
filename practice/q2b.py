"""Given an array of unique positive integers and a target value, 
print all pairs of integers from the array whose sum is equal to the target

For example::

   >>> sum_pairs([3, 2, 5, 6, 3, 5, 3], 8)
   (3, 5)
   (2, 6)
   (3, 5)
   >>> sum_pairs([1, 1, 2, 2, 2], 3)
   (1, 2)
   (1, 2)
  
   

"""


def sum_pairs(nums, target):
    avoid_list = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target and j not in avoid_list \
                and i not in avoid_list: 
                print((nums[i], nums[j]))
                avoid_list.append(i)
                avoid_list.append(j)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")