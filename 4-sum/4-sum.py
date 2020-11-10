"""
    >>> four_sum([1,0,-1,0,-2,2], 0)
    [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
"""
def four_sum(nums, target):
    """Return the numbers that sum to target."""
    ## hint to use 2 pointers -> return in ascending order
    ## get length
    final_list = []
    length = len(nums)
    if length < 4:
        return []
    nums.sort()
    for i in range(length-3):
        for j in range(i+1, length-2):
            t = target - (nums[i] + nums[j])
            low = j + 1
            high = length - 1
            while low < high:
                if nums[low] + nums[high] == t:
                    x = [nums[i], nums[j], nums[low], nums[high]]
                    if x not in final_list:
                        final_list.append(x)
                    
                    low += 1
                elif nums[low] + nums[high] < t:
                    low += 1
                else:
                    high -= 1

    return final_list



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
