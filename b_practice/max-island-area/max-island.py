class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_num = max(max_num, self.find_area(grid, i, j))
                    
        return max_num
    def find_area(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        grid[i][j] = 0
        return 1 + self.find_area(grid, i + 1, j) + self.find_area(grid, i - 1, j) + self.find_area(grid, i, j+1) +           self.find_area(grid, i, j -1)
            
        