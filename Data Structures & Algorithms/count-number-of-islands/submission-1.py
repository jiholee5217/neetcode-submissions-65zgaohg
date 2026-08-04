class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        horizontal_length = len(grid)
        vertical_length = len(grid[0])
        num_islands = 0

        def dfs(x, y):
            if x < 0 or x >= horizontal_length or y < 0 or y >= vertical_length or grid[x][y] != "1":
                return
            else:
                grid[x][y] = "0"
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x,  y + 1)
                dfs(x, y - 1)

        for x in range(horizontal_length):
            for y in range(vertical_length):
                if grid[x][y] == "1":
                    num_islands += 1
                    dfs(x, y)


        return num_islands

