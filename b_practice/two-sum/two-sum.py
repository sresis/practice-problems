class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if num_dict.get(complement) != None:
                result.append(num_dict[complement])
                result.append(i)
            num_dict[nums[i]] = i
            
        return result
            
        