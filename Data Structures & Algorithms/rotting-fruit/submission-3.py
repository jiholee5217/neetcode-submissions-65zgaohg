class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        if fresh == 0:
            return 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        minute = 0
        while queue and fresh > 0:
            level_len = len(queue)
            for _ in range(level_len):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni = i + di
                    nj = j + dj
                    if ni >= 0 and nj >=0 and ni < rows and nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
                        fresh -= 1
            minute += 1

        return minute if fresh == 0 else -1
