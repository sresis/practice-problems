"""Given an array of integers. Find the contiguous sequence with the largest sum.
Return the sum

   >>> longest_seq([2, -8, 3, -2, 4, -10])
   5
   >>> longest_seq([2, 0, 4, -1])
   6
   >>> longest_seq([-2, 8, 2, -5, 6])
   11
   >>> longest_seq([-2, 8, 2, -5, 6])
   11
   >>> longest_seq([-2, 20, -50, -5, 6])
   20


"""
def longest_seq(arr):
    longest_seq = []
    # loop through array starting at index 0
    # loop through n+1: until the curr
    # when you get to a negative number: if current sum < previous sum, start over
    all_sums = []
    #ALTERNATIVE: add every sum to  an index and take the max
    for i in range(len(arr)):
        num_sum = arr[i]
        all_sums.append(num_sum)
        for j in range(i+1,len(arr)):
            num_sum += arr[j]
            all_sums.append(num_sum)

    return max(all_sums)


   

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")