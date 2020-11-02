"""Print items in the list, using recursion.

For example::

   >>> findMin([1, 2, 3])
   1
   >>> findMin([4, 5, 6, 7, 0, 1, 2, 3])
   0

"""


def findMin(nums):
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i + 1]
        return nums[0]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. GREAT JOB!\n")