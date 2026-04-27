class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()
        dir = [[0, 1], [0, - 1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited):
                return
            visited.add((r, c))
            for dr, dc in dir:
                dfs(r + dr, c + dc)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count += 1
        return count