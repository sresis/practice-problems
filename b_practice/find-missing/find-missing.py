class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_dict = Counter(nums)
        missing = []
        for i in range(1, len(nums)+1):
            if i not in num_dict:
                missing.append(i)
        return missing
                