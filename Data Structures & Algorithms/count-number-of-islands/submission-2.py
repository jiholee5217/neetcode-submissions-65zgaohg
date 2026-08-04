class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        column_len = len(grid[0])
        
        def dfs(x, y):
            if x < 0 or x >= row_len or y < 0 or y >= column_len or grid[x][y] != '1':
                return
            else:
                grid[x][y] = '0'
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

        num_islands = 0
        for x in range(row_len):
            for y in range(column_len):
                if grid[x][y] == '1':
                    num_islands += 1
                    dfs(x, y)
                    
        return num_islands
