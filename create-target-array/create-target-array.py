class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        new_arr = []
        for i in range(len(nums)):
            if new_arr == []:
                new_arr = [nums[i]]
            elif len(new_arr) <= index[i]:
                new_arr = new_arr[:index[i]] + [nums[i]]
            else:
                new_arr = new_arr[:index[i]] + [nums[i]] +  new_arr[index[i]:] 
        return new_arr
        