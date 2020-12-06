class Solution:
    def backtrack(self, nums, visited, subset, output):
        if len(subset) == len(nums):
            output.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtrack(nums, visited, subset + [nums[i]], output)
                ## then remove it after
                visited.remove(i)
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        visited = set()
        self.backtrack(nums, visited, [], output)
        return output
        
            
        