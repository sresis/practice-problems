class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # store counts of each number
        counter = Counter(nums)
        # sort by least frequent
        nums.sort(key=lambda x: (counter[x], -x))
        return nums