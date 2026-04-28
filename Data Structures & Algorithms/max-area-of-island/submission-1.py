class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        rows, cols = len(grid), len(grid[0])
        area = 0
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
            return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)

        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area