import logging
class Solution:
    def numIslands(self, grid) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 1:
                    self.dfs(i,j)
                    count += 1
        return count 
    
    def dfs(self,i,j):
        # 从grid i 和 j 进行遍历分析
        if i < 0 or i >= self.n or j < 0 or j >= self.m or self.grid[i][j] == 0:
            return 0
        self.grid[i][j] = 0
        self.dfs(i+1,j)
        self.dfs(i,j+1)
        self.dfs(i-1,j)
        self.dfs(i,j-1)

# Path: zoo_leetcode/T200.py
grid = [[1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]]
s = Solution()
print(s.numIslands(grid))
