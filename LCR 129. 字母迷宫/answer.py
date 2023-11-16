class Solution(object):
    def wordPuzzle(self, grid, target):
        """
        :type grid: List[List[str]]
        :type target: str
        :rtype: bool
        """
        def dfs(i, j, k):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] != target[k]:
                return False
            if k == len(target) - 1: return True
            grid[i][j] = ''
            res = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            grid[i][j] = target[k]
            return res
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i, j, 0): return True
        return False
