class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # store numbers seen
        seen = set()
        # store final numbers (with 2 count)
        final_nums = []
        for i in range(len(nums)):
            if nums[i] in seen:
                final_nums.append(nums[i])
            else:
                seen.add(nums[i])
        return final_nums
            