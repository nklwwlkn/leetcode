class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        counter = 0

        def dfs(r, c, grid):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == "0":
                return 0

            visited.add((r,c))

            dfs(r + 1, c, grid)
            dfs(r - 1, c, grid)
            dfs(r, c + 1, grid)
            dfs(r, c - 1, grid)

            return 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    counter += dfs(r, c, grid)

        return counter