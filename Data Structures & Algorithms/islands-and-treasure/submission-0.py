class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        
        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if ni >= 0 and nj >= 0 and ni < rows and nj < cols and grid[ni][nj] == 2147483647:
                    grid[ni][nj] = grid[i][j] + 1
                    queue.append((ni, nj))

      
        


                