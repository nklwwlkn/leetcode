class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
    

        def dfs(r, c, p = 0):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
            
            p = dfs(r + 1, c)
            p += dfs(r - 1, c)
            p += dfs(r, c + 1)
            p += dfs(r, c - 1)

            return p

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)

        