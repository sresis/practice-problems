class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #dict key = sum
        # dict value = count
        sum_dict = {}
        sum_dict[0] = 1
        # if the sum is already in there, increment count
        curr_sum = 0
        count = 0
        for i in range(len(nums)):
            # increment current sum
            curr_sum += nums[i]
            if curr_sum - k in sum_dict:
                count += sum_dict[curr_sum - k]
                print(count)
            ## otherwise, create other dict
            if curr_sum not in sum_dict:
                sum_dict[curr_sum] = 1
            else:
                sum_dict[curr_sum] += 1
        print(sum_dict)
        return count
                
            