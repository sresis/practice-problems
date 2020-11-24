class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # go through array
        # find first instance
        position = []
        for i in range(len(nums)):
            if nums[i] == target:
                position.append(i)
                break
        # do it backwards to get last instance
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                position.append(i)
                break
        if position == []:
            return [-1, -1]
        return position
                
        