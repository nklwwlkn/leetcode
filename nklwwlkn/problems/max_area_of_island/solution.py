class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            top = dfs(r + 1, c)
            right = dfs(r, c + 1)
            down = dfs(r - 1, c)
            left = dfs(r, c - 1)

            return top + right + down + left + 1


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and not (r, c) in visited:
                    res = max(res, dfs(r, c))


        return res