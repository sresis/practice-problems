"""Given an array of unique positive integers and a target value, 
print all pairs of integers from the array whose sum is equal to the target

For example::

   >>> sum_pairs([3, 10, 2, 6, 8, 5], 8)
   (3, 5)
   (2, 6)
   >>> sum_pairs([5, 1, -2, 2, 4, 8], 3)
   (5, -2)
   (1, 2)
   >>> sum_pairs([5, 1, 3, 0, 3, 6], 6)
   (5, 1)
   (3, 3)
   (0, 6)
   

"""


def sum_pairs(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print((nums[i], nums[j]))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")