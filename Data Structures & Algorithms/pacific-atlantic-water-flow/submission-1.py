class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_queue = deque()
        atlantic_queue = deque()
        pacific = set()
        atlantic = set()

        for j in range(cols):
            pacific_queue.append((0, j))
            pacific.add((0, j))
            atlantic_queue.append((rows - 1, j))
            atlantic.add((rows - 1, j))

        for i in range(rows):
            pacific_queue.append((i, 0))
            pacific.add((i, 0))
            atlantic_queue.append((i, cols - 1))
            atlantic.add((i, cols - 1))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        while pacific_queue:
            i, j = pacific_queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni >= 0 and nj >= 0 and ni < rows and nj < cols and (ni, nj) not in pacific and heights[ni][nj] >= heights[i][j]:
                    pacific.add((ni, nj))
                    pacific_queue.append((ni, nj))
        
        while atlantic_queue:
            i, j = atlantic_queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni >= 0 and nj >= 0 and ni < rows and nj < cols and (ni, nj) not in atlantic and heights[ni][nj] >= heights[i][j]:
                    atlantic.add((ni, nj))
                    atlantic_queue.append((ni, nj))

        return [[row, col] for row, col in pacific & atlantic]
