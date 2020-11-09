class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    island_count += 1
        return island_count
    
    def dfs(self, grid, i, j):
        """Update ones we have visited """
        ## check if valid input
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != '1':
            return
        
        # reset it so we don't revisit it
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
        
        