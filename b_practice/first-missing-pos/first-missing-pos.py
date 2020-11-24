class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        # count positives
        pos = 0
        pos_num = []
        for item in nums:
            if item > 0:
                pos += 1
                pos_num.append(item)
        
        for i in range(1, len(nums)+1):
            if i not in num_set:
                return i
        print(pos_num)
        if pos == 1:
            if pos_num[0] == 1:
                return 2
            else:
                return 1
        else:
            return pos + 1